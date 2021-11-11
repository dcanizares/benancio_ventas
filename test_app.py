
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
