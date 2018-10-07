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
    process_list = simplemetrics.process()
    return jsonify(process_list)

if __name__ == '__main__':
    import os

    if not simplemetrics.hasRequirements():
        print("Exiting...")
        exit(1)

    # Development server
    # if 'DEBUG' env exist
    if os.environ.get("DEBUG"):
        if str(os.environ.get("DEBUG")).lower() == "true":
            app.run(debug=True, host='0.0.0.0', port=5000)       
        else:
            app.run(debug=False, host='0.0.0.0', port=5000)
    
    # Production server
    else:
        from waitress import serve 
        serve(app, port=5000)