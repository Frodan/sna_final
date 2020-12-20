import logging
import sys


logging.basicConfig(filename="/home/ubuntu/sna_final/log.log", level=logging.DEBUG)

try:
    import redis
    from flask import Flask, render_template
except Exception as err:
   logging.debug("Can't import libraries:")
   logging.debug(err)
   sys.exit(1)


try:
    app = Flask(__name__)
    r = redis.Redis(host="172.31.42.182", port=6379)
    r.set('counter', 0)
except Exception as err:
    ("Can not connect to DB:")
    logging.debug(err)
    sys.exit(1)


@app.route('/')
def index():
    cur = r.get('counter') if r.get('counter') else 0
    counter = int(cur) + 1
    r.set('counter', counter)
    return render_template('index.html', counter=counter)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8000)
    except Exception as err:
        logging.debug("Error in the app:")
        logging.debug(err)
        sys.exit(1)
