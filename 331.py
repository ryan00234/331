from flask import Flask, request, redirect, make_response, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

moment = Moment(app)
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent, current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

@app.route('/response')
def responser():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9527, debug=True)
