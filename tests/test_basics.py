import unittest
from flask import current_app
from src import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        pass
    
    def test_app_is_running(self):
        self.assertTrue(current_app is not None)

    def test_app_in_testing_environment(self):
        self.assertTrue(current_app.config['TESTING'])

# if __name__ == '__main__':
#     unittest.main()
