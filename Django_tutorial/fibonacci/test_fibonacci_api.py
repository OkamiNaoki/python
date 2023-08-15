import unittest
from fib import app

class TestFibonacciAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_input(self):
        response = self.app.get('/fib?n=10')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 55)

    def test_invalid_input(self):
        response = self.app.get('/fib?n=-5')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
