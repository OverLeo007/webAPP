from flask import Flask, render_template, redirect, request, send_from_directory

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/dad')
def index():
    title = 'check'
    return render_template('base.html', title=title)


@app.route("/")
def hello():
    title = 'check'
    return render_template('canvas.html')


@app.route('/ajax_handler', methods=['POST'])
def ajax_handler():
    data = request.json
    print(data)
    x, y = data['x'], data['y']
    return data


@app.route('/map/<size>')
def pixels(size):
    print(size)
    width, height = size.split('_')
    print(width, height)
    return render_template('table.html', title='пиксели', width=int(width) // 10, height=int(height) // 10)


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)


@app.route("/echo", methods=['POST'])
def echo():
    print(request.form)
    return "You said: "


if __name__ == '__main__':
    app.run(port=8090, host='127.0.0.1', debug=True)
