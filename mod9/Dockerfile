FROM python:3.10-slim-buster

RUN mkdir /app

COPY . /app/

RUN python -m pip install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python", "app.py", "-h 192.168.0.105"]