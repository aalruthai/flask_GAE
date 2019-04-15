from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/p2')
def hello_2():
    abort(404)
    return 'h2'


if __name__ == '__main__':
    app.run()