import json
import logging

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.debug('hello endpoint was reached')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.debug('status endpoint was reached')
    return app.response_class(response=json.dumps({"result": "OK - healthy"}),status=200,mimetype='application/json')

@app.route("/metrics")
def metrics():
    app.logger.debug('metrics endpoint was reached')
    return app.response_class(response=json.dumps({"data": {"UserCount": "140", "UserCountActive": "23"}}),
                              status=200,mimetype='application/json')




if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG,format="%(asctime)s, %(message)s ")

    app.run(host='0.0.0.0')
