from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>Game 1</h1>'