import datetime
import os
import random
from datetime import datetime, timedelta
from flask import Flask, url_for
import re
from flask import jsonify


app = Flask(__name__)
list_cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
list_cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
visits = 0


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return ', '.join(list_cars)


@app.route('/cats')
def cats():
    return random.choice(list_cats)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.now()
    current_time_after_hour = current_time + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/counter')
def counter():
    global visits
    visits += 1
    return str(visits)


@app.errorhandler(404)
def page_not_found(error):
    links = []
    for endpoint in app.url_map._rules_by_endpoint.keys():
        if "static" not in endpoint:
            href = url_for(endpoint)
            link = f"<a href='{href}'>{endpoint}</a>"
            links.append(link)
    return f"<h1>Упс... Похоже сраницы не существует</h1><p>Попробуйте перейти на одну из следующих страниц:</p>{'<br>'.join(links)}"


if __name__ == '__main__':
    app.run()
