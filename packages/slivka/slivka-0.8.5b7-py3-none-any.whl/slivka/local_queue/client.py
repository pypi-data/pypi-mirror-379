import atexit
import re
import threading
from collections import namedtuple

import zmq

zmq_ctx = zmq.Context()
atexit.register(zmq_ctx.destroy, 0)


class LocalQueueClient(threading.local):
    JobStatusResponse = namedtuple("JobStatus", 'id, state, returncode')

    def __init__(self, address, secret=None):
        threading.local.__init__(self)
        if not re.match(r'(\w*:)?//', address):
            # if only host given, assume tcp://
            address = "tcp://" + address
        elif address.startswith('unix://'):
            address = str.replace(address, 'unix', 'ipc', 1)
        self.address = address
        self.secret = secret
        self.socket = zmq_ctx.socket(zmq.REQ)
        self.socket.setsockopt(zmq.RCVTIMEO, 100)
        self.socket.setsockopt(zmq.REQ_RELAXED, 1)
        self.socket.connect(self.address)

    def submit_job(self, cmd, cwd, env):
        try:
            self.socket.send_json(
                {'method': 'POST', 'cmd': cmd, 'cwd': cwd, 'env': env},
                flags=zmq.NOBLOCK
            )
            response = self.socket.recv_json()
        except zmq.error.Again:
            raise ConnectionError(
                "Queue server at %s is not responding." % self.address
            ) from None
        if response.pop('ok'):
            return self.JobStatusResponse(**response)
        else:
            raise RequestError(response['error'])

    def get_job_status(self, id):
        self.socket.send_json({'method': 'GET', 'id': id})
        response = self.socket.recv_json()
        if response.pop('ok'):
            return self.JobStatusResponse(**response)
        else:
            raise RequestError(response['error'])

    def cancel_job(self, id):
        self.socket.send_json({'method': 'CANCEL', 'id': id})
        response = self.socket.recv_json()
        if response.pop('ok'):
            return True
        else:
            raise RequestError(response['error'])

    def release_job(self, id):
        self.socket.send_json({'method': 'DELETE', 'id': id})
        response = self.socket.recv_json()
        if response.pop('ok'):
            return True
        else:
            raise RequestError(response['error'])


class RequestError(RuntimeError):
    pass
