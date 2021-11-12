from flask import Flask, Response, request

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

@app.route('/saluda/<nombre>')
def saluda(nombre):
    return f'Hola soy {nombre}'

@app.route('/suma', methods=['POST'])
def suma():
    datos = request.get_json()
    suma = int(datos["primer_numero"]) + int(datos["segundo_numero"])

    return Response(response=str(suma), status=201)