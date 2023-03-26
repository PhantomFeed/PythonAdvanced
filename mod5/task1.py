import os
import shlex
import subprocess
from flask import Flask
import signal


app = Flask(__name__)


def release_port(port: int):
    command_str = f'lsof -i :{port}'
    command = shlex.split(command_str)
    res = subprocess.run(command, capture_output=True)
    result = res.stdout.decode().split('\n')[1:-1]
    pids = []
    for i in result:
        pids.append(int(i.split()[1]))

    if not os.getpid() in pids:
        for pid in pids:
            os.kill(pid, signal.SIGKILL)
    app.run(port=port, debug=True)


if __name__ == '__main__':
    release_port(5000)
