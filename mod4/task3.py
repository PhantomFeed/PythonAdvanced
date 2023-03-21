from flask import Flask
from datetime import timedelta


app = Flask(__name__)


@app.route('/uptime', methods=['GET'])
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds=uptime_seconds)).split('.')[0]
    return f"Current uptime is {uptime}"


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
