# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import simplemetrics

app = Flask(__name__)


@app.route("/")
def hello_world():
    return simplemetrics.hello()

@app.route("/metrics/cpu")
def metrics_cpu():
    cpu = simplemetrics.cpu()
    return jsonify(cpu)

@app.route("/metrics/ram")
def metrics_ram():
    memory = simplemetrics.memory()
    return jsonify(memory)

@app.route("/metrics/disk")
def metrics_disk():
    disks = simplemetrics.disks()
    return jsonify(disks)

@app.route("/metrics/network")
def metrics_network():
    network = simplemetrics.network()
    return jsonify(network)

@app.route("/metrics/services")
def metrics_services():
    process_list = simplemetrics.services()
    return jsonify(process_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
