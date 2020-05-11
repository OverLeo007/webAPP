from flask import Flask, render_template, redirect, request, send_from_directory
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def handler():
    req = request.get_json(force=True)
    print(req)
    return json.dumps(req['color'])


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(port=8090, host='127.0.0.1', debug=True)
