from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = numbers.split('/')
    dic = []
    for num in numbers:
        if num.isdecimal():
            dic.append(int(num))
        else:
            return 'В URL передано не число'
    num = max(dic)
    return f'Максимальное число: <i>{num}</i>'


if __name__ == '__main__':
    app.run()
