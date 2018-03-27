# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import temp

device_id = '192.168.17.157:5555'

app = Flask(__name__)
# app.config.from_object('config')

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


@app.route('/debug2')
def debug2():
    return render_template('debug_connection_172.html')


@app.route('/SQL')
def sql():
    return render_template('SQL.html')


@app.route('/test')
def test():
    # device = request.args.get('device', 0, type=str)
    temp.os.popen('adb connect ' + device_id)
    return render_template('temp.html')


@app.route('/device')
def device_set():
    global device_id
    device = request.args.get('device', '')
    temp.os.popen('adb connect ' + device)
    device_id = device
    max1 = temp.os.popen('adb -s ' + device_id + ' shell getprop|grep heapgrowthlimit').readline()
    max2 = temp.os.popen('adb -s ' + device_id + ' shell getprop|grep dalvik.vm.heapstartsize').readline()
    max3 = temp.os.popen('adb -s ' + device_id + ' shell getprop|grep dalvik.vm.heapsize').readline()
    return jsonify(max1=max1[-8:], max2=max2[-8:], max3=max3[-8:])


@app.route('/cpu_info')
def cpu_info():
    cpu = temp.cpu(device_id)
    return jsonify(cpu=cpu)


@app.route('/mem_info')
def mem_info():
    mem = temp.mem(device_id)
    return jsonify(mem=mem)


@app.route('/Android')
def android():
    return render_template('Android.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
