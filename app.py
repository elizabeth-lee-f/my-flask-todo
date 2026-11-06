from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Привет. Это моё Flask-приложение в Docker</h1>'

@app.route('/todo')
def todo():
    return '<h2>Мой список задач:</h2><ul><li>Создать проект</li><li>Написать Dockerfile</li><li>Собрать и запустить</li></ul>'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=7345)