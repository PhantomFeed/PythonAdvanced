from flask import Flask

app = Flask(__name__)
storage = {}


@app.route('/add/<int:date>/<int:expense>')
def saver(date, expense):
    if len(str(date)) == 8:
        date = str(date)
        year, month = date[:4], date[4:6]
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += expense
        return 'Информация сохранена!'


@app.route('/calculate/<int:year>')
def calculate_for_year(year):
    months = storage[str(year)]
    total = sum([expense for key, expense in months.items()])
    return f'Суммарные траты за указанный год: {total}'


@app.route('/calculate/<int:year>/<int:month>')
def calculate_year_and_month(year, month):
    return f'Суммарные траты за указанные год и месяц: {storage[str(year)][str(month)]}'


if __name__ == '__main__':
    app.run(debug=True)
