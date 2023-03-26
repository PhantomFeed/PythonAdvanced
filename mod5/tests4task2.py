import unittest
from mod5.task2 import app


class TestCodeForm(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/run_code'

    def test_can_work_correctly(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")', 'timeout': 10})
        assert response.status_code == 200

    def test_can_throw_error_if_timeout_lower(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")', 'timeout': -10})
        assert response.status_code == 400

    def test_can_throw_error_if_timeout_bigger(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")', 'timeout': 40})
        assert response.status_code == 400

    def test_can_throw_error_if_timeout_incorrect(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")', 'timeout': 'ten'})
        assert response.status_code == 400

    def test_can_throw_error_if_code_incorrect(self):
        response = self.app.post(self.base_url, data={'code': 'p123rint\'(24"He21llo"1)', 'timeout': 10})
        self.assertTrue('SyntaxError' in response.text)

    def test_can_throw_error_if_code_is_empty(self):
        response = self.app.post(self.base_url, data={'timeout': 10})
        assert response.status_code == 400

    def test_can_work_without_timeout(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")'})
        assert response.status_code == 200

    def test_if_killed_by_timeout(self):
        response = self.app.post(self.base_url, data={'code': 'print("Hello")', 'timeout': 0})
        self.assertTrue('True' in response.text)

    def test_unsafe_request(self):
        response = self.app.post(self.base_url, data={"code": 'from subprocess import run\nrun([\'./kill_the_system.sh\'])', 'timeout': 10})
        self.assertTrue('Resource temporarily unavailable' in response.text)
