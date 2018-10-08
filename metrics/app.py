# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort

import simplemetrics, auth

app = Flask(__name__)

@app.route("/")
def hello_world():
    if not auth.validate():
        abort(401)

    return "I want coffee."

@app.route("/metrics/cpu")
def metrics_cpu():
    if not auth.validate():
        abort(401)

    cpu = simplemetrics.cpu()
    return jsonify(cpu)

@app.route("/metrics/ram")
def metrics_ram():
    if not auth.validate():
        abort(401)

    memory = simplemetrics.memory()
    return jsonify(memory)

@app.route("/metrics/disk")
def metrics_disk():
    if not auth.validate():
        abort(401)
        
    disks = simplemetrics.disks()
    return jsonify(disks)

@app.route("/metrics/network")
def metrics_network():
    if not auth.validate():
        abort(401)

    network = simplemetrics.network()
    return jsonify(network)

@app.route("/metrics/services")
def metrics_services():
    if not auth.validate():
        abort(401)
        
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