import unittest
from mod3.task4 import Person


class TestPersonApp(unittest.TestCase):
    def test_can_get_correct_person_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        person.name = 'Владислав'
        person.yob = 2002
        person.address = ''
        person1 = person
        self.assertTrue(person1.name == 'Владислав' and person1.yob == 2002 and person1.address == '')

    def test_can_get_age_correct_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        self.assertEqual(person.get_age(), 20)

    def test_can_get_correct_name_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        self.assertEqual(person.get_name(), 'Данила')

    def test_can_set_name_correctly_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        person.set_name('Владислав')
        self.assertEqual(person.name, 'Владислав')

    def test_can_set_address_correctly_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        person.set_address('')
        self.assertEqual(person.address, '')

    def test_can_get_correct_address_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003, address='Have')
        self.assertEqual(person.get_address(), 'Have')

    def test_can_return_homeless_person_in_mod3_task4(self):
        person = Person(name='Данила', year_of_birth=2003)
        self.assertTrue(person.is_homeless())