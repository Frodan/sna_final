import redis
from flask import Flask, render_template


app = Flask(__name__)
r = redis.Redis(host="172.31.42.182", port=6379)

r.set('counter', 0)

@app.route('/')
def index():
    counter = int(r.get('counter')) + 1
    r.set('counter', counter)
    return render_template('index.html', counter=counter)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
