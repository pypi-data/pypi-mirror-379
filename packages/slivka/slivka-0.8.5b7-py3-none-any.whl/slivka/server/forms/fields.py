import itertools
import os
import typing
from abc import ABC
from base64 import urlsafe_b64encode
from collections import OrderedDict
from functools import partial
from typing import Union, List

import pymongo.database
from bson import ObjectId
from werkzeug.datastructures import FileStorage, MultiDict

import slivka
import slivka.db
from slivka.db.documents import UploadedFile
from slivka.db.helpers import insert_one
from slivka.utils import expression_parser, media_types
from .file_proxy import FileProxy
from .widgets import *

__all__ = [
    'BaseField', 'ArrayFieldMixin',
    'IntegerField', 'IntegerArrayField',
    'DecimalField', 'DecimalArrayField',
    'TextField', 'TextArrayField',
    'BooleanField', 'BooleanArrayField',
    'FlagField', 'FlagArrayField',
    'ChoiceField', 'ChoiceArrayField',
    'FileField', 'FileArrayField',
    'ValidationError'
]


class BaseField:
    """ Base class for form fields providing validation and conversion

    Field objects are contained within the form and are used to
    retrieve data from the requests, validate and convent the values
    to python and convert them to strings.
    All form field classes must inherit from this class and call its
    constructor. The subclasses may override :py:meth:`run_validation`
    for custom value validation. The parameters for the fields are
    provided from the configuration file.

    :param id: field identifier
    :param name: human readable name/label
    :param description: longer, human readable description
    :param default: default value for the field
    :param required: whether the field is required
    :param condition: logical expression involving other fields
    """

    def __init__(self,
                 id,
                 name='',
                 description='',
                 default=None,
                 required=True,
                 condition=None):
        self.id = id
        self.name = name
        self.description = description
        self.default = default
        self.required = required and default is None
        self.condition = (None if condition is None
                          else expression_parser.Expression(condition))
        self._widget = None

    def fetch_value(self, data: MultiDict, files: MultiDict):
        """
        Retrieves value from the request data. This value will
        be further passed to the validation method. The deriving
        classes may need to override this method i.e. for file
        retrieval, see :py:method:`FileField.value_from_request_data`.

        :param data: request POST data
        :param files: request multipart-POST files
        :return: retrieved raw value
        """
        return data.get(self.id)

    def run_validation(self, value):
        """ Validates the value and converts to Python value.

        Checks whether the value meets the field type and constraints.
        Otherwise, raises :py:class:`ValidationError`.
        Subclasses may override this method with their implementation
        of validation, but the value should be converted with
        their superclass' :py:meth:`run_validation` method first.

        :param value: value to be validated and converted
        :return: converted value
        """
        if hasattr(value, '__len__') and len(value) == 0:
            return None
        else:
            return value

    def validate(self, value):
        """ Runs validation of the value.

        Used by form during :py:meth:`BaseForm.full_clean`to check
        and convert the data from the HTTP request.
        Performs the validation of the value obtained form
        :py:meth:`fetch_value` and returns the value
        converted to the appropriate Python type.
        It takes care of arrays by validating each value individually.

        This method is final and must not be overridden!

        :param value: the value or list of values to be validated
        :return: validated value
        :raise ValidationError: provided value is not valid
        """
        value = self.run_validation(value)
        if value is None and self.required:
            raise ValidationError("Field is required", 'required')
        return value

    def _check_default(self):
        """ Passes the default value through validation.

        It should be called at the end of `__init__` after all the
        validators and default value are set up.

        :raise RuntimeError: default value is invalid
        """
        if self.default is not None:
            try:
                self.run_validation(self.default)
            except ValidationError as e:
                raise ValidationError(
                    "Invalid default value for field %s" % self.name
                ) from e

    def test_condition(self, values):
        if self.condition:
            return self.condition.evaluate({
                'self': values[self.id], **values
            })
        else:
            return True

    def to_arg(self, value) -> Union[None, str, List[str]]:
        """ Converts value to argument or list of arguments.

        This method is used to convert values to the command line
        arguments just before saving them to the database.
        By default, it returns the string representation of the
        ``value``, but subclasses may implement different behaviour

        :param value: a value to be converted
        :return: one or multiple command line arguments
        """
        return str(value) if value is not None else None

    def __json__(self):
        """ Json representation of the field as shown to the client. """
        return {
            'type': 'undefined',
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'required': self.required,
            'array': self.is_array,
            'default': self.default
        }

    @property
    def widget(self):
        raise NotImplementedError

    @property
    def input_tag(self):
        return self.widget.render()

    @property
    def is_array(self):
        return False


class ArrayFieldMixin(BaseField, ABC):
    def fetch_value(self, data: MultiDict, files: MultiDict):
        """ Retrieves multiple values from the request data. """
        return [v for v in data.getlist(self.id) if v is not None] or None

    def validate(self, value):
        """ Runs validation for each value in the list. """
        if value is None:
            return super(ArrayFieldMixin, self).validate(None)
        value = [val for val in value if val is not None]
        if len(value) == 0:
            return super(ArrayFieldMixin, self).validate(None)
        return [super(ArrayFieldMixin, self).validate(val) for val in value]

    def to_arg(self, value) -> Union[None, str, List[str]]:
        """ Converts each value in the list to cmd arg. """
        if value is None:
            return None
        converted = (
            super(ArrayFieldMixin, self).to_arg(val)
            for val in value
        )
        args = [val for val in converted if val is not None]
        return args if len(args) > 0 else None

    def _check_default(self):
        """ Checks the default value which is an array. """
        if self.default is not None:
            if isinstance(self.default, list):
                try:
                    for val in self.default:
                        self.run_validation(val)
                except ValidationError as e:
                    raise ValidationError(
                        "Invalid default value for '%s'." % self.name
                    ) from e
            else:
                raise ValidationError("Default value for '%s' must be an array.")

    @property
    def is_array(self):
        return True


class IntegerField(BaseField):
    """ Represents a field that takes an integer value.

    :param id: name of the field
    :param min: minimum value or None if unbound
    :param max: maximum value or None if unbound
    :param **kwargs: see arguments of :py:class:`BaseField`
    """

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id,
                 min=None,
                 max=None,
                 **kwargs):
        super().__init__(id, **kwargs)
        self.__validators = []
        self.min = min
        self.max = max
        if max is not None:
            self.__validators.append(partial(_max_value_validator, max))
        if min is not None:
            self.__validators.append(partial(_min_value_validator, min))
        self._check_default()

    @property
    def widget(self):
        if self._widget is None:
            widget = NumberInputWidget(self.id)
            widget['min'] = self.min
            widget['max'] = self.max
            widget['step'] = 1
            widget['value'] = self.default
            widget['required'] = self.required
            self._widget = widget
        return self._widget

    def run_validation(self, value):
        value = super().run_validation(value)
        if value is None:
            return None
        try:
            if (isinstance(value, bool) or
                    (isinstance(value, float) and not value.is_integer())):
                raise TypeError
            value = int(value)
        except (ValueError, TypeError):
            raise ValidationError("Invalid integer value", 'invalid')
        for validator in self.__validators:
            validator(value)
        return value

    def __json__(self):
        j = super().__json__()
        j['type'] = 'integer'
        if self.min is not None: j['min'] = self.min
        if self.max is not None: j['max'] = self.max
        return j


class IntegerArrayField(ArrayFieldMixin, IntegerField):
    pass


class DecimalField(BaseField):
    """ Represents a field that takes a floating point number.

    :param id: name of the field
    :param min: minimum value or None if unbound
    :param max: maximum value or None if unbound
    :param min_exclusive: whether min is excluded, default False
    :param max_exclusive: whether max is excluded, default False
    :param **kwargs: see arguments of :py:class`BaseClass`
    """

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id,
                 min=None,
                 max=None,
                 min_exclusive=False,
                 max_exclusive=False,
                 **kwargs):
        super().__init__(id, **kwargs)
        self.__validators = []
        self.min = min
        self.max = max
        self.min_exclusive = min_exclusive
        self.max_exclusive = max_exclusive
        if max is not None:
            validator = (_exclusive_max_value_validator
                         if max_exclusive else _max_value_validator)
            self.__validators.append(partial(validator, max))
        if min is not None:
            validator = (_exclusive_min_value_validator
                         if min_exclusive else _min_value_validator)
            self.__validators.append(partial(validator, min))
        self._check_default()

    @property
    def widget(self):
        if self._widget is None:
            widget = NumberInputWidget(self.id)
            widget['min'] = self.min
            widget['max'] = self.max
            widget['step'] = 'any'
            widget['value'] = self.default
            widget['required'] = self.required
            self._widget = widget
        return self._widget

    def run_validation(self, value):
        value = super().run_validation(value)
        if value is None:
            return None
        try:
            if isinstance(value, bool):
                raise TypeError
            value = float(value)
        except (ValueError, TypeError):
            raise ValidationError("Invalid decimal number", 'invalid')
        for validator in self.__validators:
            validator(value)
        return value

    def __json__(self):
        j = super().__json__()
        j['type'] = 'decimal'
        if self.max is not None: j['max'] = self.max
        if self.min is not None: j['min'] = self.min
        if self.min_exclusive is not None and self.min:
            j['minExclusive'] = self.min_exclusive
        if self.max_exclusive is not None and self.max:
            j['maxExclusive'] = self.max_exclusive
        return j


class DecimalArrayField(ArrayFieldMixin, DecimalField):
    pass


class TextField(BaseField):
    """ Represents a field taking an text value.

    :param id: name of the field
    :param min_length: minimum length of text
    :param max_length: maximum length of text
    :param **kwargs: see arguments of :py:class:`BaseField`
    """

    def __init__(self,
                 id,
                 min_length=None,
                 max_length=None,
                 **kwargs):
        super().__init__(id, **kwargs)
        self.__validators = []
        self.min_length = min_length
        self.max_length = max_length
        if min_length is not None:
            self.__validators.append(partial(
                _min_length_validator, min_length
            ))
        if max_length is not None:
            self.__validators.append(partial(
                _max_length_validator, max_length
            ))
        self._check_default()

    @property
    def widget(self):
        if self._widget is None:
            self._widget = TextInputWidget(self.id)
            self._widget['value'] = self.default
            self._widget['required'] = self.required
        return self._widget

    def run_validation(self, value):
        value = super().run_validation(value)
        if value is None:
            return None
        value = str(value)
        for validator in self.__validators:
            validator(value)
        return value

    def __json__(self):
        j = super().__json__()
        j['type'] = 'text'
        if self.min_length is not None: j['minLength'] = self.min_length
        if self.max_length is not None: j['maxLength'] = self.max_length
        return j


class TextArrayField(ArrayFieldMixin, TextField):
    pass


class BooleanField(BaseField):
    """ Represents a field taking a boolean value.

    The field interprets any string defined in a ``FALSE_STR`` set
    as well as anything that evaluates to False as False.

    :param id: field name
    :param **kwargs: see arguments of :py:class:`BaseField`
    """
    FALSE_STR = {'no', 'false', '0', 'n', 'f', 'none', 'null', 'off'}

    def __init__(self, id, **kwargs):
        super().__init__(id, **kwargs)
        self._check_default()

    @property
    def widget(self):
        if self._widget is None:
            self._widget = CheckboxInputWidget(self.id, value='true')
            self._widget['checked'] = bool(self.default)
            self._widget['required'] = self.required
        return self._widget

    def run_validation(self, value):
        value = super().run_validation(value)
        if isinstance(value, str) and value.lower() in self.FALSE_STR:
            value = False
        return True if value else None

    def to_arg(self, value) -> Union[None, str, List[str]]:
        if isinstance(value, str) and value.lower() in self.FALSE_STR:
            value = False
        return 'true' if value else None

    def __json__(self):
        j = super().__json__()
        j['type'] = 'flag'
        return j


class BooleanArrayField(ArrayFieldMixin, BooleanField):
    pass


FlagField = BooleanField
FlagArrayField = BooleanArrayField
""" An alias for the BooleanField """


class ChoiceField(BaseField):
    """ Represents a field taking one of the available options.

    The choices mapping is used to convert the value to the
    command line parameter.

    :param id: field name
    :param choices: a mapping of user choices to the cmd values
    :param **kwargs: see arguments of :py:class:`BaseField`
    """

    def __init__(self,
                 id,
                 choices=(),
                 **kwargs):
        super().__init__(id, **kwargs)
        self.__validators = []
        self.choices = OrderedDict(choices)
        self.__validators.append(partial(
            _choice_validator,
            self.choices.keys()
        ))
        self._check_default()

    @property
    def widget(self):
        if self._widget is None:
            self._widget = SelectWidget(self.id, options=self.choices)
            self._widget['required'] = self.required
            self._widget['multiple'] = isinstance(self, ArrayFieldMixin)
        return self._widget

    def run_validation(self, value):
        """
        Checks if the value is in either choices keys or values,
        validation fails otherwise
        """
        # FIXME: should also convert the value here
        value = super().run_validation(value)
        if value is None:
            return None
        for validator in self.__validators:
            validator(value)
        return value

    def to_arg(self, value):
        """ Converts value to the cmd argument using choices map"""
        return self.choices.get(value, value)

    def __json__(self):
        j = super().__json__()
        j['type'] = 'choice'
        j['choices'] = list(self.choices)
        return j


class ChoiceArrayField(ArrayFieldMixin, ChoiceField):
    pass


class FileField(BaseField):
    """ Represents a field taking a file.

    The file can be supplied as a uuid or :py:class:`werkzeug.FileStorage`.
    The values are converted to a :py:class:`FileProxy` convenience
    wrapper.

    :param id: field name
    :param media_type: accepted media (content) type; used in file
        content validation
    :param media_type_parameters: additional parameters regarding
        file content; used solely as a hint
    :param extensions: accepted file extensions; used solely as a hint
    :param **kwargs: see arguments of :py:class:`BaseField`
    """

    def __init__(self,
                 id,
                 media_type=None,
                 media_type_parameters=(),
                 extensions=(),
                 **kwargs):
        assert kwargs.get('default') is None
        super().__init__(id, **kwargs)
        self.__validators = []
        self.extensions = extensions
        self.media_type = media_type
        self.media_type_parameters = media_type_parameters or {}
        if media_type is not None:
            self.__validators.append(partial(
                _media_type_validator, media_type
            ))

    def fetch_value(self, data: MultiDict, files: MultiDict):
        return files.get(self.id) or data.get(self.id)

    @property
    def widget(self):
        if self._widget is None:
            widget = FileInputWidget(self.id)
            widget['accept'] = str.join(
                ',', ('.%s' % ext for ext in self.extensions)
            )
            self._widget = widget
        return self._widget

    def run_validation(self, value) -> typing.Optional['FileProxy']:
        """
        Validates and converts ``value`` to the :py:class:`FileProxy`
        object. The value can be a :py:class:`FileProxy` which will
        be returned directly, a :py:class:`werkzeug.FileStorage`
        object which will be wrapped in :py:class:`FileProxy`
        or a file id in which case a database lookup is performed
        to find the path that will be used to construct a
        :py:class:`FileProxy`.

        :param value: file from the request or file id
        :return: a wrapper around the file
        """
        value = super().run_validation(value)
        if value is None:
            return None
        elif isinstance(value, FileStorage):
            file = FileProxy(file=value)
        elif isinstance(value, str):
            file = FileProxy.from_id(value, slivka.db.database)
            if file is None:
                raise ValidationError("File not found.", 'not_found')
        elif isinstance(value, FileProxy):
            file = value
        else:
            raise TypeError("Invalid type %s" % type(value))
        for validator in self.__validators:
            validator(file)
        return file

    def __json__(self):
        j = super().__json__()
        j['type'] = 'file'
        if self.media_type is not None:
            j['mimetype'] = self.media_type
            j['mediaType'] = self.media_type
            j['mediaTypeParameters'] = self.media_type_parameters
        if self.extensions: j['extensions'] = self.extensions
        return j

    def to_arg(self, value: 'FileProxy'):
        """ Converts FileProxy to cmd argument.

        The file is written to teh disk if not saved already
        and its path is returned.
        """
        if not value:
            return None
        if value.path is None:
            raise ValueError("file has no path")
        return value.path


class FileArrayField(ArrayFieldMixin, FileField):
    def fetch_value(self, data: MultiDict, files: MultiDict):
        return (files.getlist(self.id) + data.getlist(self.id)) or None


# Helper methods that are used for value validation.

def _max_value_validator(limit, value):
    if value > limit:
        raise ValidationError(
            "Value must be less than or equal to %s" % limit, 'max_value'
        )


def _min_value_validator(limit, value):
    if value < limit:
        raise ValidationError(
            "Value must be greater than or equal to %s" % limit, 'min_value'
        )


def _exclusive_max_value_validator(limit, value):
    if value >= limit:
        raise ValidationError(
            "Value must be less than %s" % limit, 'max_value'
        )


def _exclusive_min_value_validator(limit, value):
    if value <= limit:
        raise ValidationError(
            "Value must be greater than %s" % limit, 'min_value'
        )


def _min_length_validator(limit, value):
    if len(value) < limit:
        raise ValidationError(
            "Value is too short. Min %d characters" % limit, 'min_length'
        )


def _max_length_validator(limit, value):
    if len(value) > limit:
        raise ValidationError(
            "Value is too long. Max %d characters" % limit, 'max_length'
        )


def _choice_validator(choices, value):
    if value not in choices:
        raise ValidationError(
            "Value \"%s\" is not one of the available choices." % value,
            'invalid'
        )


def _media_type_validator(media_type, file: FileProxy):
    file.reopen()
    if not media_types.validate(media_type, file):
        raise ValidationError(
            "The file is not a valid %s type" % media_type, 'media_type'
        )


class ValidationError(ValueError):
    """ Exception raised when value validation fails. """

    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code
