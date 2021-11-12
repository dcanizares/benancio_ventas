import json
from os import error
import unittest
from app import app

class Test_App(unittest.TestCase):
    def setUp(self):
        # Es necesario instanciar un cliente de testing de la app
        self.app = app.test_client()

    def test_endpoint_raiz_devuelve_h1_game_1_y_status_200(self):
        # "Tiro un request" (entre comillas porque no es un request real) a la url raíz y obtengo la respuesta
        response = self.app.get("/")

        # Verifico que la respuesta sea la que espero (hay que decodificarla con .decode porque viene como string binario)
        self.assertEqual('<h1>Game 1</h1>', response.data.decode("utf-8"))

        # Verifico que el código de respuesta sea 200
        self.assertEqual(200, response.status_code)

    def test_endpoint_iri_devuelve_h1_hola_soy_iruuu_y_status_200(self):

        response = self.app.get('/iri')

        self.assertEqual('<h1>Hola soy Iruuu</h1>', response.data.decode("utf-8"))

        self.assertEqual(200, response.status_code)

    def test_endpoint_charly_devuelve_h1_hola_soy_charly_y_status_200(self):

        response = self.app.get('/charly')

        self.assertEqual('<h1>Hola soy Charly</h1>', response.data.decode("utf-8"))

        self.assertEqual(200, response.status_code) 

    def test_endpoint_saludar_con_parametro_devuelve_h1_con_parametro(self):
        response = self.app.get('/saluda/rogelio')

        self.assertEqual('Hola soy rogelio', response.data.decode("utf-8"))

        self.assertEqual(200, response.status_code)

    def test_post_endpoint_suma_con_2_y_3_retorna_5(self):
        response = self.app.post(
            "/suma",
            data=json.dumps({"primer_numero":3, "segundo_numero": 2}),
            content_type="application/json"
        )
        self.assertEqual(json.dumps({"resultado":5}), response.data.decode("utf-8"))
        self.assertEqual(201, response.status_code)

    def test_post_endpoint_suma_con_10_y_20_retorna_30(self):
        response = self.app.post(
            "/suma",
            data=json.dumps({"primer_numero":10, "segundo_numero": 20}),
            content_type="application/json"
        )
        self.assertEqual(json.dumps({"resultado":30}), response.data.decode("utf-8"))
        self.assertEqual(201, response.status_code)

    def test_post_endpoint_resta_5_y_3_retorna_2(self):
        response = self.app.post(
            "/resta",
            data = json.dumps({"primer_numero": 5, "segundo_numero": 3}),
            content_type = "application/json"
        )
        self.assertEqual(json.dumps({"resultado":2}), response.data.decode("utf-8"))
        self.assertEqual(201, response.status_code)
    
    def test_post_endpoint_producto_11_y_3_retorna_33(self):
        response = self.app.post(
            "/producto",
            data = json.dumps({"primer_numero": 11, "segundo_numero": 3}),
            content_type = "application/json"
        )
        self.assertEqual(json.dumps({"resultado": 33}), response.data.decode("utf-8"))
        self.assertEqual(201, response.status_code)

    def test_post_endpoint_razon_20_entre_5_retorna_4_y_status_200(self):
        response = self.app.post(
            "/razon",
            data = json.dumps({"primer_numero": 20, "segundo_numero": 5}),
            content_type = "application/json"
        )
        self.assertEqual(json.dumps({"resultado": 4}), response.data.decode("utf-8"))
        self.assertEqual(201, response.status_code)

    def test_post_endpoint_razon_entre_10_y_0_retorna_status_400(self):
        response = self.app.post(
            "/razon",
            data = json.dumps({"primer_numero": 10, "segundo_numero": 0}),
            content_type = "application/json"
        )
        self.assertEqual(json.dumps({"error": "Vuelva a la escuela!"}), response.data.decode("utf-8"))
        self.assertEqual(400, response.status_code)