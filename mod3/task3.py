import unittest
import mod2.task7
from mod2.task7 import app


class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/'
        mod2.task7.storage = {'2023':
                                  {'01': 15000,
                                   '02': 7500,
                                   '03': 3300,
                                   '04': 45000,
                                   '05': 9000,
                                   '06': 13000,
                                   '07': 61000,
                                   '08': 85000,
                                   '09': 22000,
                                   '10': 19000,
                                   '11': 8000,
                                   '12': 0
                                   }
                              }

    def test_can_work_correctly_in_saver(self):
        response = self.app.get(self.base_url + 'add/20230306/2500')
        self.assertEqual(mod2.task7.storage['2023']['03'], 5800)

    def test_can_throws_date_error_correctly_in_saver(self):
        response = self.app.get(self.base_url + 'add/2023aa01/2500')
        self.assertRaises(TypeError)

    def test_can_throws_finance_error_correctly_in_saver(self):
        response = self.app.get(self.base_url + 'add/20231101/9s9s51')
        self.assertRaises(TypeError)

    def test_can_works_correctly_calculate_by_year(self):
        response = self.app.get(self.base_url + 'calculate/2023')
        response_text = response.data.decode()
        self.assertTrue('287800' in response_text)

    def test_can_throws_year_error_correctly_in_calculate_by_year(self):
        with self.assertRaises(KeyError) as raises:
            response = self.app.get(self.base_url + 'calculate/1010')

    def test_can_throws_year_error_correctly_if_storage_empty_in_calculate_by_year(self):
        mod2.task7.storage = {}
        with self.assertRaises(KeyError) as raises:
            response = self.app.get(self.base_url + 'calculate/2222')

    def test_can_calculate_correctly_in_calculate_year_and_month(self):
        response = self.app.get(self.base_url + 'calculate/2023/10')
        response_text = response.data.decode()
        self.assertTrue('19000' in response_text)

    def test_can_throws_type_error_correctly_in_calculate_by_year_and_month(self):
        response = self.app.get(self.base_url + 'calculate/2023/0b')
        self.assertRaises(TypeError)

    def test_can_throws_month_error_correctly_in_calculate_by_year_month(self):
        with self.assertRaises(KeyError) as raises:
            response = self.app.get(self.base_url + 'calculate/2023/44')
