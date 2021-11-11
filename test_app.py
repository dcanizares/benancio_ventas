
import unittest
from app import app

class Test_App(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_endpoint_raiz_devuelve_h1_game_1_y_status_200(self):
        response = self.app.get("/")

        self.assertEqual('<h1>Game 1</h1>', response.data.decode("utf-8"))
        self.assertEqual(200, response.status_code)
