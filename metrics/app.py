# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import psutil, statistics

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
    cpu['per_cpu'] = psutil.cpu_percent(interval=1, percpu=True)
    cpu['total'] = statistics.median(cpu['per_cpu'])
    return jsonify(cpu)


@app.route("/metrics/ram")
def metrics_ram():
    memory = {}
    memory['virtual'] = psutil.virtual_memory()._asdict()
    memory['swap'] = psutil.swap_memory()._asdict()
    return jsonify(memory)


@app.route("/metrics/disk")
def metrics_disk():
    disks = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if "tmpfs" in partition.device:
            continue
        disks[partition.device] = {
            'device' : partition.device,
            'usage' : psutil.disk_usage(partition.mountpoint)._asdict()
        }
    return jsonify(disks)


def getNetworkStats (nothing):
    network = {}
    network['interfaces'] = psutil.net_io_counters(pernic=True)
    for key, value in network['interfaces'].items():
        network['interfaces'][key] = value._asdict()
    # network['connections'] = []
    # for connection in psutil.net_connections():
    #     network['connections'].append(connection._asdict())
    print("sonho")
    import json
    return json.loads(json.dumps(network))
@app.route("/metrics/network")
def metrics_network():
    from multiprocessing import Pool
    p = Pool(processes=20)
    data = p.map(getNetworkStats, [1])
    p.close()
    return jsonify(data[0])

@app.route("/metrics/services")
def metrics_services():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
