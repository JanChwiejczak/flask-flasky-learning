from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def agent():
    user_agent = request.headers.get('User-Agent')
    return "Hello world, your browser is {}".format(user_agent)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/cookie')
def response_cookie():
    response = make_response('This doc carries cookie')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)
