from flask import Flask, render_template, request, jsonify
import random
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
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

@app.route('/dynamic')
def add_numbers():
    label = ["January", "February", "March", "April", "May", "June", "July"]
    data1 = random.sample(range(100), 7)
    data2 = random.sample(range(100), 7)
    return jsonify(label, data1, data2)

@app.route('/Android')
def Android():
    return render_template('Android.html',)

@app.route('/debug2')
def debug2():
    return render_template('debug_connection_172.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9527, debug=True)
