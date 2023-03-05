import datetime
import os
import random
from datetime import datetime, timedelta
from flask import Flask
import re

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


def read_txt(filename):
    global war_and_peace
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)

    with open(BOOK_FILE) as book:
        war_and_peace = book.read()
        war_and_peace = re.findall('[a-zа-яё]+', war_and_peace, flags=re.IGNORECASE)
    return war_and_peace


war_and_peace = read_txt('war_and_peace.txt')


@app.route('/get_random_word')
def random_word():
    return random.choice(war_and_peace)


@app.route('/counter')
def counter():
    global visits
    visits += 1
    return str(visits)


if __name__ == '__main__':
    app.run()
