from flask import Flask, render_template, jsonify
import psutil
import platform
import socket
import time
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    return jsonify({
        "cpu_percent": psutil.cpu_percent(),
        "cpu_per_core": psutil.cpu_percent(percpu=True),
        "memory": {
            "percent": psutil.virtual_memory().percent,
            "used": round(psutil.virtual_memory().used / (1024 ** 3), 2),
            "total": round(psutil.virtual_memory().total / (1024 ** 3), 2)
        },
        "disk": {
            "percent": psutil.disk_usage('/').percent,
            "used": round(psutil.disk_usage('/').used / (1024 ** 3), 2),
            "total": round(psutil.disk_usage('/').total / (1024 ** 3), 2)
        },
        "network": psutil.net_io_counters()._asdict(),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "uptime": str(uptime).split('.')[0]
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
