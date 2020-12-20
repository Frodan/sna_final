import redis
from flask import Flask, render_template
import logging

Logging.basicConfig(filename="/home/ubuntu/sna_final/log.log", level=(logging.INFO, logging.DEBUG, logging.ERROR))

try:
    app = Flask(__name__)
    r = redis.Redis(host="172.31.42.182", port=6379)
    r.set('counter', 0)
except Exception as err:
   logging.debug(err)

@app.route('/')
def index():
    counter = int(r.get('counter')) + 1
    r.set('counter', counter)
    return render_template('index.html', counter=counter)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8000)
    except Exception as err:
        logging.debug(err)
