import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)



@app.route('/')
def hello():
    with open('/tmp/files/file.text') as f:
        content = f.read().splitlines()
    count = get_hit_count()
    return 'Hello World! I have been seen {} times. File content:{}\n'.format(count,content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
