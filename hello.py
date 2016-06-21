from datetime import datetime

from flask import Flask, request, make_response, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = "kljhk^%^;:jas76478tgfy;//z"
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return "Hello world, your browser is {}".format(user_agent)

@app.route('/time')
def index_time():
    return render_template('index_time.html', current_time=datetime.utcnow())

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)

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
