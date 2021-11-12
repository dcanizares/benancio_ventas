from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>Game 1</h1>'


@app.route('/iri')
def iri():
    return '<h1>Hola soy Iruuu</h1>'

@app.route('/charly')
def charly():
    return '<h1>Hola soy Charly</h1>'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Hola soy {nombre}'

