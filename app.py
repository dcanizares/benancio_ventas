from flask import Flask, Response, request, jsonify
import json

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
    respuesta = {"resultado": suma}

    return json.dumps(respuesta), 201    # manera fea: return Response(response=json.dumps(respuesta), status=201)

@app.route('/resta', methods = ['POST'])
def resta():
    datos = request.get_json()
    resta = int(datos["primer_numero"]) - int(datos["segundo_numero"])
    respuesta = {"resultado" : resta}

    return json.dumps(respuesta), 201

@app.route('/producto', methods = ['POST'])
def producto():
    datos = request.get_json()
    producto = int(datos["primer_numero"]) * int(datos["segundo_numero"])
    respuesta = {"resultado" : producto}

    return json.dumps(respuesta), 201