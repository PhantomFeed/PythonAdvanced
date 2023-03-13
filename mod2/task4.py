from flask import Flask
from datetime import datetime

app = Flask(__name__)
weekdays_tuple = ('понедельника', 'ворника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресения')
weekdays_ending = ('его', 'его', 'ей', 'его', 'ей', 'ей', 'его')


@app.route('/hello-world/<username>')
def hello_world(username):
    weekday = weekdays_tuple[datetime.today().weekday()]
    ending = 'ей' if weekday[-1] == 'ы' else 'его'
    return f'Привет, {username}. Хорош{ending} {weekday}'


if __name__ == '__main__':
    app.run(debug=True)
