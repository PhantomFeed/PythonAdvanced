from flask import Flask

app = Flask(__name__)
storage = {}


def saver(date, number):
    if len(str(date)) == 8:
        date = str(date)
        storage.setdefault(date[:4], {}).setdefault(date[4:6], 0)
        storage[date[:4]][date[4:6]] += number
        return 'Информация сохранена'


@app.route('/calculate/<int:year>')
def calculator_for_year(year):
    months = storage[str(year)]
    total = sum([number for key, number in months.items()])
    return f'Суммарные траты за указанный год: {total}'


@app.route('/calculate/<int:year>/<int:month>')
def calculator_year_and_month(year, month):
    return f'Суммарные траты за указанные год и месяц: {storage[str(year)][str(month)]}'


if __name__ == '__main__':
    app.run()
