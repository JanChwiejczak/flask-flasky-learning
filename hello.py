from datetime import datetime

from flask import Flask, request, make_response, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return "Hello world, your browser is {}".format(user_agent)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/cookie')
def response_cookie():
    response = make_response('This doc carries cookie')
    response.set_cookie('answer', '42')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
