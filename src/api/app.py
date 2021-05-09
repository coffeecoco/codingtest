from flask import Flask, jsonify
from flask import request

import os
try:
    from environment import payload
except ImportError:
    from .environment import payload
try:
    from environment import payload
    from loghandler.logger import info, log_error
except ImportError:
    from .environment import payload
    from .loghandler.logger import info, log_error

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_api_hello():
    info("Executed")
    return "Hello World"

@app.route('/status', methods=['GET'])
def get_api():
    info("Executed")
    return jsonify(payload)

@app.errorhandler(404)
def resource_not_found(e):
    log_error(f"{e.code}, {e.name}")
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    log_level = payload['myapplication'][0]['log_level']
    app.run(debug=log_level,host='0.0.0.0',port=5000)
