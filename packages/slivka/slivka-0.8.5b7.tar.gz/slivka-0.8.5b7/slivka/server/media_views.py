import os

import flask


def serve_uploads_view(file_path):
    return flask.send_from_directory(
        directory=flask.current_app.config['uploads_dir'],
        path=file_path
    )


def serve_results_view(file_path):
    return flask.send_from_directory(
        directory=flask.current_app.config['jobs_dir'],
        path=file_path
    )
