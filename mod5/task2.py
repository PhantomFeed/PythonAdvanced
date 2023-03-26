import shlex
import subprocess
from typing import Tuple
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10, validators=[NumberRange(min=0, max=30)])


def python_code_is_subprocess(code: str, timeout: int) -> Tuple[str, str, bool]:
    command = f'prlimit --nproc=1:1 python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    killed_by_timout = False
    try:
        outs, errs = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
        killed_by_timout = True
    return outs.decode(), errs.decode(), killed_by_timout


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        stdout, stderr, killed = python_code_is_subprocess(code=code, timeout=timeout)
        return f'Stdout: {stdout} stderr: {stderr}, process was killed by timeout: {killed}'
    return f'Bad request. Error = {form.errors}', 400


if __name__ == '__main__':
    app.run(debug=True)