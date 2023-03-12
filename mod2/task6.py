from flask import Flask
import os

app = Flask(__name__)


@app.route('/file_preview/<int:SIZE>/<path:RELATIVE_PATH>')
def file_preview(SIZE, RELATIVE_PATH):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ABS_PATH = os.path.join(BASE_DIR, RELATIVE_PATH)
    with open(ABS_PATH) as book:
        result_text = book.read(SIZE)
    result_size = len(result_text)
    return f'<b>{ABS_PATH}</b> {result_size}<br>{result_text}'


if __name__ == '__main__':
    app.run(debug=True)