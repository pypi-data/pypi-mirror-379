import filecmp
import os
import tempfile
from unittest import mock

import pytest

import slivka.db.repositories
from slivka.conf import ServiceConfig
from slivka.db.repositories import FilesRepository
from slivka.scheduler import Runner
from slivka.scheduler.runners import Command, Job
from slivka.scheduler.runners.runner import format_symlink_name
from test.conftest import job_directory

Argument = ServiceConfig.Argument


@pytest.fixture()
def global_env(request):
    append_env = {}
    if hasattr(request, "param") and request.param:
        append_env = request.param
    else:
        mark = request.node.get_closest_marker("env")
        if mark and mark.kwargs:
            append_env = mark.kwargs
    with mock.patch.dict(os.environ, append_env) as env:
        yield env


@pytest.fixture()
def command_arguments(request):
    mark = request.node.get_closest_marker("runner")
    if mark and "args" in mark.kwargs:
        return mark.kwargs["args"]
    if hasattr(request, "param"):
        return request.param
    return []


@pytest.fixture(params=[{}])
def command_env(request):
    return request.param


@pytest.fixture()
def command_consts(request):
    mark = request.node.get_closest_marker("runner")
    if mark and "consts" in mark.kwargs:
        return mark.kwargs["consts"]
    if hasattr(request, "param"):
        return request.param
    return {}


@pytest.fixture()
def runner(
        global_env,
        command_arguments,
        command_consts,
        command_env,
        database,
        slivka_home
):
    return Runner(
        runner_id=None,
        files_repository=FilesRepository(
            slivka_home / "uploads",
            slivka_home / "jobs",
            database
        ),
        command="example",
        args=command_arguments,
        consts=command_consts,
        outputs=[],
        env=command_env,
    )


class TestSingleInputInterpolation:
    @pytest.fixture()
    def command_arguments(self, request):
        marker = request.node.get_closest_marker("argument")
        arg_template = marker.args[0]
        return [Argument("input", arg_template, **marker.kwargs)]

    @pytest.fixture()
    def command_env(self):
        return {"EXAMPLE": "example.bin"}

    @pytest.mark.argument("$(value)")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("val", ["val"]),
            ("my value", ["my value"]),
            ('"my value"', ['"my value"']),
            ("", [""]),
            ('my "special" value', ['my "special" value']),
            ("my 'special' value", ["my 'special' value"]),
            ("$SLIVKA_HOME", ["$SLIVKA_HOME"]),
            ("$MY_VAR", ["$MY_VAR"]),
            ("~", ["~"]),
            ("${HOME}", ["${HOME}"]),
        ],
    )
    def test_build_args_if_plain_value(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("--option=$(value)")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("val", ["--option=val"]),
            ("my value", ["--option=my value"]),
            ('"my value"', ['--option="my value"']),
            ("", ["--option="]),
            ('my "special" value', ['--option=my "special" value']),
            ("my 'special' value", ["--option=my 'special' value"]),
            ("$SLIVKA_HOME", ["--option=$SLIVKA_HOME"]),
            ("$MY_VAR", ["--option=$MY_VAR"]),
            ("~", ["--option=~"]),
            ("${HOME}", ["--option=${HOME}"]),
        ],
    )
    def test_build_args_if_char_delimited(
        self, runner, value, expected_command
    ):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("--option $(value)")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("val", ["--option", "val"]),
            ("my value", ["--option", "my value"]),
            ('"my value"', ["--option", '"my value"']),
            ("", ["--option", ""]),
            (
                'my "special" value',
                ["--option", 'my "special" value'],
            ),
            (
                "my 'special' value",
                ["--option", "my 'special' value"],
            ),
            ("$SLIVKA_HOME", ["--option", "$SLIVKA_HOME"]),
            ("$MY_VAR", ["--option", "$MY_VAR"]),
            ("~", ["--option", "~"]),
            ("${HOME}", ["--option", "${HOME}"]),
        ],
    )
    def test_build_args_if_space_delimited(
        self, runner, value, expected_command
    ):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("'--option $(value)'")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("val", ["--option val"]),
            ("my value", ["--option my value"]),
            ("'my value'", ["--option 'my value'"]),
        ],
    )
    def test_build_args_if_option_single_quoted(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument('"--option $(value)"')
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("val", ["--option val"]),
            ("my value", ["--option my value"]),
            ("'my value'", ["--option 'my value'"]),
        ],
    )
    def test_build_args_if_option_double_quoted(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("--option")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("true", ["--option"]),
            (None, []),
            (False, []),
        ],
    )
    def test_build_args_if_flag(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("-v$(value)", default="defvalue")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("foo", ["-vfoo"]),
            ("", ["-v"]),
            (None, ["-vdefvalue"]),
        ],
    )
    def test_build_args_default_present(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.env(VAR="VAR_VALUE")
    @pytest.mark.argument("--env=$VAR")
    def test_build_args_if_arg_contains_system_var(self, runner):
        assert runner.build_args({"input": "true"}) == ["--env=VAR_VALUE"]

    @pytest.mark.argument("--home=$SLIVKA_HOME")
    def test_build_args_if_arg_contains_slivka_home(self, runner, slivka_home):
        assert runner.build_args({"input": "true"}) == [f"--home={slivka_home}"]

    @pytest.mark.argument("--bin=$EXAMPLE")
    def test_build_args_if_arg_contains_local_val(self, runner, global_env):
        assert runner.build_args({"input": "true"}) == ["--bin=example.bin"]

    @pytest.mark.argument("$(value)", symlink="input.in")
    @pytest.mark.parametrize(
        "value, expected_command",
        [
            ("input.in", ["input.in"]),
            (None, []),
        ],
    )
    def test_build_args_if_symlink(self, runner, value, expected_command):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("$(value)")
    @pytest.mark.parametrize(
        "value, expected_command",
        [(["a", "b", "c", "d"], ["a", "b", "c", "d"])],
    )
    def test_build_args_if_multiple_values(
        self, runner, value, expected_command
    ):
        assert runner.build_args({"input": value}) == expected_command

    @pytest.mark.argument("-m=$(value)")
    def test_build_args_if_multiple_values_parameter_repeated(self, runner):
        args = runner.build_args({"input": ["a", "b", "c"]})
        assert args == ["-m=a", "-m=b", "-m=c"]

    @pytest.mark.argument("-m=$(value)", join=",")
    def test_build_args_if_multiple_values_joined_with_character(self, runner):
        args = runner.build_args({"input": ["a", "b", "c"]})
        assert args == ["-m=a,b,c"]

    @pytest.mark.argument("-m $(value)", join=" ")
    def test_build_args_if_multiple_values_joined_with_space(self, runner):
        args = runner.build_args({"input": ["a", "b", "c"]})
        assert args == ["-m", "a b c"]


@pytest.mark.parametrize("command_env", [{}])
@pytest.mark.parametrize(
    "command_arguments",
    [
        [
            Argument("opt0", "-i $(value)"),
            Argument("opt1", "-o $(value)"),
            Argument("opt2", "-a $(value)"),
            Argument("flag0", "--flag"),
            Argument("arg0", "$(value)"),
        ]
    ],
)
@pytest.mark.parametrize(
    "values, expected_command",
    [
        ({}, []),
        (
            {"opt0": "inp", "arg0": "argv", "flag0": "true"},
            ["-i", "inp", "--flag", "argv"],
        ),
        (
            {
                "opt0": "inp",
                "opt1": "out",
                "opt2": "app",
                "flag0": "true",
                "arg0": "argv",
            },
            ["-i", "inp", "-o", "out", "-a", "app", "--flag", "argv"],
        ),
    ],
)
def test_multiple_arguments_interpolation(runner, values, expected_command):
    assert runner.build_args(values) == expected_command


@pytest.mark.parametrize(
    "command_arguments, command_consts, expected_command",
    [
        (
            [Argument("myarg", "-a=$(value)")],
            {"myarg": "const-val"},
            ["-a=const-val"]
        ),
        (
            [Argument("myarg", "-a=$(value)")],
            {},
            []
        ),
        (
            [Argument("myarg", "-a=$(value)", default="def-value")],
            {"myarg": "const-val"},
            ["-a=const-val"]
        )
    ]
)
def test_constant_arguments(runner, expected_command):
    assert runner.build_args({}) == expected_command


class TestEnvVariables:
    def test_slivka_home_variable_set(self, slivka_home, runner):
        assert runner.env["SLIVKA_HOME"] == str(slivka_home)

    @pytest.mark.env(BIN_PATH="/usr/local/bin")
    @pytest.mark.parametrize(
        "command_env, expected_path",
        [({"COMMAND": "$BIN_PATH/program"}, "/usr/local/bin/program")],
    )
    def test_variable_reference(self, runner, expected_path):
        assert runner.env["COMMAND"] == expected_path

    @pytest.mark.parametrize(
        "command_env",
        [{"VAR": "$MISSING"}, {"VAR": "$VAR_B", "VAR_B": "value"}],
    )
    def test_missing_variable_reference(self, runner):
        assert runner.env["VAR"] == ""

    @pytest.mark.env(GLOBAL="global")
    def test_global_variables_not_propagated(self, runner):
        assert "GLOBAL" not in runner.env

    @pytest.mark.env(PATH="/usr/bin:/usr/local/bin:/bin")
    def test_path_variable_set(self, runner):
        assert runner.env["PATH"] == "/usr/bin:/usr/local/bin:/bin"

    @pytest.mark.env(GLOBAL="global")
    @pytest.mark.parametrize(
        "command_env, expected_global, expected_ref",
        [
            ({}, None, None),
            ({"GLOBAL": "local"}, "local", None),
            ({"GLOBAL": "local", "REF": "$GLOBAL"}, "local", "global"),
        ],
    )
    def test_global_variable_overridden(
        self, runner, expected_global, expected_ref
    ):
        assert runner.env.get("GLOBAL") == expected_global
        assert runner.env.get("REF") == expected_ref


@pytest.fixture()
def mock_submit():
    with mock.patch("slivka.scheduler.runners.Runner.submit") as mock_func:
        yield mock_func


def test_start_submit_command_if_no_parameters(
    runner, job_directory, mock_submit
):
    assert runner.submit is mock_submit
    mock_submit.side_effect = lambda cmd: Job("0xc0ffee", cmd.cwd)
    runner.start({}, job_directory)
    mock_submit.assert_called_once_with(Command(["example"], job_directory))


@pytest.mark.runner(
    args=[
        Argument("opt0", "-p0 $(value)"),
        Argument("opt1", "-p1 $(value)"),
        Argument("arg0", "$(value)"),
        Argument("const0", "$(value)", default="out.txt"),
    ]
)
def test_start_submit_command_if_parameters_present(
    job_directory, runner, mock_submit
):
    assert runner.submit is mock_submit
    runner.start({"opt0": "foo", "opt1": "bar", "arg0": "xxx"}, job_directory)
    mock_submit.assert_called_once_with(
        Command(
            ["example", "-p0", "foo", "-p1", "bar", "xxx", "out.txt"],
            job_directory,
        )
    )

@pytest.mark.runner(
    args=[Argument("_const",  "-c=$(value)")],
    consts={"_const": "const-val"}
)
def test_start_submit_using_runner_constants(
    job_directory, runner, mock_submit
):
    assert runner.submit is mock_submit
    mock_submit.return_value = Job("0x00000", job_directory)
    runner.start({}, job_directory)
    mock_submit.assert_called_once_with(
        Command(["example", "-c=const-val"], job_directory)
    )


def test_start_returns_job_id(runner, job_directory, mock_submit):
    assert runner.submit is mock_submit
    mock_submit.return_value = Job("0xc0ffee", job_directory)
    assert runner.start({}, job_directory) == Job("0xc0ffee", job_directory)


@pytest.mark.runner(args=[Argument("input", "$(value)", symlink="input.txt")])
def test_start_creates_file_link(job_directory, runner, mock_submit):
    infile = tempfile.NamedTemporaryFile()
    infile.write(b"hello world\n")
    infile.flush()
    mock_submit.return_value = Job("", job_directory)
    runner.start({"input": infile.name}, job_directory)
    link_path = os.path.join(job_directory, "input.txt")
    assert filecmp.cmp(infile.name, link_path), "Files are not identical"


@pytest.mark.runner(
    args=[Argument("input", "$(value)", symlink="$(filename.stem).input.yaml")]
)
def test_start_create_file_link_symlink_template(
    job_directory, runner, mock_submit
):
    infile = tempfile.NamedTemporaryFile(prefix="data.")
    infile.write(b"hello world\n")
    infile.flush()
    mock_submit.return_value = Job("", job_directory)
    runner.start({"input": infile.name}, job_directory)
    link_path = os.path.join(job_directory, "data.input.yaml")
    assert filecmp.cmp(infile.name, link_path), "Files are not identical"


def test_batch_start_submits_commands(
    runner, job_directory_factory, mock_submit
):
    n = 5
    inputs = [{} for _ in range(n)]
    cwds = [job_directory_factory() for _ in range(n)]
    mock_submit.side_effect = [Job("%04d" % i, cwds[i]) for i in range(n)]
    runner.batch_start(inputs, cwds)
    mock_submit.assert_has_calls(
        [mock.call(Command(["example"], cwds[i])) for i in range(n)],
        any_order=True,
    )


@pytest.mark.runner(args=[Argument("opt0", "-i $(value)")])
def test_batch_start_with_parameters_submits_commands(
    runner, job_directory_factory, mock_submit
):
    n = 5
    inputs = [{"opt0": "val%d" % i} for i in range(n)]
    cwds = [job_directory_factory() for _ in range(n)]
    mock_submit.side_effect = [Job("%04d" % i, cwds[i]) for i in range(n)]
    runner.batch_start(inputs, cwds)
    mock_submit.assert_has_calls(
        [
            mock.call(Command(["example", "-i", "val%d" % i], cwds[i]))
            for i in range(n)
        ]
    )

@pytest.mark.parametrize(
    'file',
    [
        FilesRepository.File(
            path="/var/slivka/example/data.txt",
            title=None,
            media_type="text/plain"
        ),
        FilesRepository.File(
            path="/var/slivka/example/job/xyz/outfile",
            title="data.txt",
            media_type="text/plain"
        )
    ],
    ids=["untitled_file", "titled_file"]
)
@pytest.mark.parametrize(
    ("template", "expected_name"),
    [
        pytest.param("input.txt", "input.txt", id="no_interpolation"),
        pytest.param("$(filename)", "data.txt", id="filename"),
        pytest.param("$(filename.stem)", "data", id="stem"),
        pytest.param("$(filename.ext)", ".txt", id="ext"),
        pytest.param("$(filename.stem)$(filename.ext)", "data.txt", id="stem+ext"),
        pytest.param("$(filename).input", "data.txt.input", id="embedded_filename"),
        pytest.param("$(filename.stem).input", "data.input", id="embedded_stem"),
        pytest.param("input$(filename.ext)", "input.txt", id="embedded_ext"),
        pytest.param("$(tomato.stem)", "$(tomato.stem)", id="invalid_identifier"),
        pytest.param("input.%03d.txt", "input.001.txt", id="with_index"),
    ]
)
def test_format_symlink_name(file, template, expected_name):
    assert format_symlink_name(template, file, 1) == expected_name
