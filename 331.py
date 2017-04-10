from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500

@app.route('/debug')
def debug():
    return render_template('debug_ui_172.html')

@app.route('/SQL')
def SQL():
    return render_template('SQL.html')

@app.route('/test')
def test():
    return render_template('temp.html')

@app.route('/Android')
def Android():
    return render_template('Android.html')

@app.route('/debug2')
def debug2():
    return render_template('debug_connection_172.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9527, debug=True)
