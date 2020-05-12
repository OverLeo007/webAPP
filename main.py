from flask import Flask, render_template, request, send_from_directory
import json
from data import db_session
from data.fieldItem import Item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def handler():
    req = request.get_json(force=True)
    cell = Item()
    x, y = (req['x'] + 10) // 10, (req['y'] + 10) // 10
    cell.color = req['color']
    cell.index = (x - 1) * 70 + y - 1
    print(x, y)
    session = db_session.create_session()
    session.add(cell)
    session.commit()
    return json.dumps({'status': 'success'})


@app.route('/cells', methods=['GET'])
def get_cells():
    session = db_session.create_session()
    jsonn = session.query(Item).all()
    print(*jsonn, sep='\n')
    session.commit()
    return str(jsonn)


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)


def clear_db():
    session = db_session.create_session()
    for item in session.query(Item).all():
        session.delete(item)
    session.commit()


if __name__ == '__main__':
    db_session.global_init("db/items.sqlite")
    app.run(port=8090, host='127.0.0.1', debug=True)
    # clear_db()
