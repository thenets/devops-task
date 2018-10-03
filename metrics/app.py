# -*- coding: utf-8 -*-

from flask import Flask
import psutil, statistics, json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/hello/<name>")
def say_hello(name):
    return f"Hello <b>{name}</b>"


@app.route("/metrics/cpu")
def metrics_cpu():
    cpu = {}
    cpu['per_cpu'] = psutil.cpu_percent(interval=1, percpu=True)._asdict()
    cpu['total'] = statistics.median(cpu['per_cpu'])
    return json.dumps(cpu)


@app.route("/metrics/ram")
def metrics_ram():
    memory = {}
    memory['virtual'] = psutil.virtual_memory()._asdict()
    memory['swap'] = psutil.swap_memory()._asdict()
    return json.dumps(memory)


@app.route("/metrics/disk")
def metrics_disk():
    pass


@app.route("/metrics/network")
def metrics_network():
    pass


@app.route("/metrics/services")
def metrics_services():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
