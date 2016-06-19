from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/<name>')
def user(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
