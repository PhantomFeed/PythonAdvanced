from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field, ValidationError
from wtforms.validators import InputRequired, Email, NumberRange
from datetime import timedelta

app = Flask(__name__)


def number_length(min: int, max: int, message: Optional[str] = 'Number is invalid'):
    def _number_length(form: FlaskForm, field: Field):
        if len(str(field.data)) > max or len(str(field.data)) < min:
            raise ValidationError(message=message)
    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = 'Number is invalid'):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data)) > self.max or len(str(field.data)) < self.min:
            raise ValidationError(message=self.message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 10), NumberLength(10, 10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Successfully registered user {email} with phone +7{phone}'
    return f'Invalid input, {form.errors}', 400


@app.route('/uptime', methods=['GET'])
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds=uptime_seconds)).split('.')[0]
    return f"Current uptime is {uptime}"


# @app.route('/ps', methods=['GET'])
# def


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
