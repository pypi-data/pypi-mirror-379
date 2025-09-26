import os.path
from unittest import mock

import bson
import pytest

from slivka import JobStatus
from slivka.db.documents import JobRequest
from slivka.db.helpers import delete_many, insert_many, pull_many
from slivka.db.repositories import FilesRepository
from slivka.scheduler import Runner, Scheduler
from slivka.scheduler.runners import Job, RunnerID
from slivka.scheduler.scheduler import (
    ERROR,
    REJECTED,
    ExecutionDeferred,
    ExecutionFailed,
    SelectorContext,
)
from test.tools import anything, in_any_order


@pytest.fixture
def new_runner(database, slivka_home):
    files_repo = FilesRepository(
        slivka_home / "uploads",
        slivka_home / "jobs",
        database
    )
    def factory(
        service,
        name,
        command=None,
        args=None,
        consts=None,
        env=None,
        selector_options=None,
    ):
        return Runner(
            RunnerID(service, name),
            files_repository=files_repo,
            command=command or [],
            args=args or [],
            consts=consts or {},
            outputs=[],
            env=env or {},
            selector_options=selector_options or {},
        )
    return factory


@pytest.fixture()
def mock_batch_start():
    with mock.patch.object(Runner, "batch_start") as mock_method:
        yield mock_method


@pytest.fixture()
def mock_check_status():
    with mock.patch.object(Runner, "check_status") as mock_method:
        yield mock_method


@pytest.fixture()
def mock_submit():
    with mock.patch.object(Runner, "submit") as mock_method:
        yield mock_method


def test_group_requests(job_directory, new_runner):
    scheduler = Scheduler(job_directory)
    runner1 = new_runner("example", "runner1")
    runner2 = new_runner("example", "runner2")
    scheduler.add_runner(runner1)
    scheduler.add_runner(runner2)
    scheduler.selectors["example"] = lambda inputs: inputs.get("use")

    requests = [
        JobRequest(service="example", inputs={"use": "runner1"}),
        JobRequest(service="example", inputs={"use": "runner2"}),
        JobRequest(service="example", inputs={"use": None}),
        JobRequest(service="example", inputs={"use": "runner1"}),
    ]
    grouped = scheduler.group_requests(requests)
    assert grouped == {
        runner1: in_any_order(requests[0], requests[3]),
        runner2: in_any_order(requests[1]),
        REJECTED: in_any_order(requests[2]),
    }


def test_group_requests_with_context_data(job_directory, new_runner):
    scheduler = Scheduler(job_directory)
    runner1 = new_runner("example", "runner1", selector_options={"strlen": 3})
    runner2 = new_runner("example", "runner2", selector_options={"strlen": 5})

    def selector(inputs, context: SelectorContext):
        strlen = len(inputs["str"])
        for runner in context.runners:
            ctx_data = context.runner_options[runner]
            if strlen <= ctx_data["strlen"]:
                return runner

    scheduler.add_runner(runner1)
    scheduler.add_runner(runner2)
    scheduler.add_selector("example", selector)

    requests = [
        JobRequest(service="example", inputs={"str": "xyz"}),
        JobRequest(service="example", inputs={"str": "xyzt"}),
        JobRequest(service="example", inputs={"str": "abcxyz"}),
        JobRequest(service="example", inputs={"str": "abc"}),
    ]
    grouped = scheduler.group_requests(requests)
    assert grouped == {
        runner1: in_any_order(requests[0], requests[3]),
        runner2: in_any_order(requests[1]),
        REJECTED: in_any_order(requests[2]),
    }


def test_group_requests_if_runner_does_not_exist(job_directory, new_runner):
    scheduler = Scheduler(job_directory)
    runner1 = new_runner("example", "runner1")
    scheduler.add_runner(runner1)
    scheduler.selectors["example"] = lambda inputs: "runner2"

    requests = [JobRequest(service="example", inputs={})]
    grouped = scheduler.group_requests(requests)
    assert grouped == {ERROR: in_any_order(*requests)}


def create_requests(count=1, service="example"):
    return [
        JobRequest(
            _id=bson.ObjectId(), service=service, inputs={"input": "val%d" % i}
        )
        for i in range(count)
    ]


def test_start_requests_if_successful_start(job_directory, mock_batch_start, new_runner):
    scheduler = Scheduler(job_directory)
    runner = new_runner("example", "example")
    requests = [
        JobRequest(
            _id=bson.ObjectId(), service="example", inputs={"input": "val"}
        ),
        JobRequest(
            _id=bson.ObjectId(), service="example", inputs={"input": "val2"}
        ),
    ]
    mock_batch_start.side_effect = lambda inputs, cwds: (
        [Job("%04x" % i, cwd) for i, cwd in enumerate(cwds)]
    )
    started = scheduler._start_requests(runner, requests)
    assert started == in_any_order(
        *((req, Job("%04x" % i, anything())) for i, req in enumerate(requests))
    )


def test_start_requests_deferred_execution_if_error_raised(
    job_directory, mock_batch_start, new_runner
):
    scheduler = Scheduler(job_directory)
    runner = new_runner("example", "example")
    requests = create_requests(2)
    mock_batch_start.side_effect = OSError
    with pytest.raises(ExecutionDeferred):
        scheduler._start_requests(runner, requests)


def test_start_request_failed_execution_if_too_many_errors_raised(
    job_directory, mock_batch_start, new_runner
):
    scheduler = Scheduler(job_directory)
    runner = new_runner("example", "example")
    requests = create_requests(3)
    scheduler.set_failure_limit(0)
    mock_batch_start.side_effect = OSError
    with pytest.raises(ExecutionFailed):
        scheduler._start_requests(runner, requests)


def test_start_request_job_directory_is_job_id(
    job_directory, mock_batch_start, new_runner
):
    scheduler = Scheduler(job_directory)
    runner = new_runner("example", "example")
    requests = create_requests(1)
    mock_batch_start.side_effect = lambda inputs, cwds: (
        [Job("%04x" % i, cwd) for i, cwd in enumerate(cwds)]
    )
    scheduler._start_requests(runner, requests)
    req_id = requests[0].b64id
    path = os.path.join(job_directory, req_id[-2:], req_id[-4:-2], req_id[:-4])
    mock_batch_start.assert_called_with(
        [{"input": "val0"}],
        [path]
    )


class TestJobStatusUpdates:
    @pytest.fixture()
    def requests(self, database):
        requests = create_requests(5)
        insert_many(database, requests)
        yield requests
        delete_many(database, requests)

    @pytest.fixture()
    def scheduler(self, job_directory, new_runner):
        scheduler = Scheduler(job_directory)
        runner = new_runner("example", "example")
        scheduler.add_runner(runner)
        scheduler.selectors["example"] = lambda inputs: "example"
        return scheduler

    @pytest.mark.parametrize("status", list(JobStatus))
    def test_check_status_updates_requests(
        self,
        scheduler,
        requests,
        database,
        mock_batch_start,
        mock_check_status,
        status,
    ):
        # must start the job, before moving to status check stage
        mock_batch_start.side_effect = lambda inputs, cwds: (
            [Job("%04x" % i, cwd) for i, cwd in enumerate(cwds)]
        )
        mock_check_status.return_value = status
        scheduler.main_loop()
        pull_many(database, requests)
        assert all(req.state == status for req in requests)

    def test_submit_deferred_job_status_not_updated(
        self, scheduler, requests, database, mock_submit
    ):
        mock_submit.side_effect = OSError
        scheduler.main_loop()
        pull_many(database, requests)
        assert all(req.state == JobStatus.ACCEPTED for req in requests)

    def test_submit_failed_job_status_set_to_error(
        self, scheduler, requests, database, mock_submit
    ):
        mock_submit.side_effect = OSError
        scheduler.set_failure_limit(0)
        scheduler.main_loop()
        pull_many(database, requests)
        assert all(req.state == JobStatus.ERROR for req in requests)
