import unittest
from mod4.app import app


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/registration'

    def test_can_work_correctly(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 200

    def test_can_throws_email_error(self):
        response = self.app.post(self.base_url, data={'email': 'danilaurfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_mail_is_num(self):
        response = self.app.post(self.base_url, data={'email': 98760, 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_email_is_empty(self):
        response = self.app.post(self.base_url, data={'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_phone_smaller(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 987654321,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_phone_bigger(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 98765432100,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_phone_is_word(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 'qwerty',
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_phone_is_empty(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru',
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_name_is_num(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 987654310,
                                                      'name': 123456, 'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_name_is_empty(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 987654310,
                                                      'address': 'Екатеринбург', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_address_is_num(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 987654310,
                                                      'address': 123456, 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_address_is_empty(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'index': 123456,
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_index_is_word(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 'qwerty',
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_index_is_empty(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург',
                                                      'comment': 'kwarg'})
        assert response.status_code == 400

    def test_can_throws_error_if_comment_is_empty(self):
        response = self.app.post(self.base_url, data={'email': 'danila@urfu.ru', 'phone': 9876543210,
                                                      'name': 'Данила', 'address': 'Екатеринбург', 'index': 123456})
        assert response.status_code == 200
