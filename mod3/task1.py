import unittest
from mod2.task4 import app, weekdays_tuple
from datetime import datetime
from freezegun import freeze_time


class TestWeekdayApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_username_in_task4(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_weekday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    def test_can_get_correct_weekday_if_username_is_weekday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'Хорошей среды')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-02")
    def test_can_get_correct_monday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-03")
    def test_can_get_correct_tuesday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-04")
    def test_can_get_correct_wednesday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-05")
    def test_can_get_correct_thursday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-06")
    def test_can_get_correct_friday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-07")
    def test_can_get_correct_saturday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)

    @freeze_time("2023-01-08")
    def test_can_get_correct_sunday_in_task4(self):
        day = weekdays_tuple[datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(day in response_text)
