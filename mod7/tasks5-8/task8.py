from flask import Flask, request
from logging import config
from dictConfig import *


app = Flask(__name__)
logger = logging.getLogger('FlaskLogger')
logging.config.dictConfig(dict_config)


@app.route("/save_log", methods=['POST'])
def log_collector():
    data = request.form.to_dict()
    print(data)
    with open("./server.log", "a+") as logger:
        log = f"{data['levelname']} | {data['name']} | {data['asctime']} | {data['lineno']} | {data['msg']}\n"
        logger.write(log)


@app.route("/get_log", methods=['GET'])
def get_log() -> str:
    with open("./server.log", "r") as log:
        a = log.read()
        # return log.read()
    return f'<pre>{a}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
