import unittest
from mod5.task3 import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_can_ignir_error(self):
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            print('Выполнено без ошибок')
            assert True
        except:
            assert False

    def test_can_pushed_higher_errors(self):
        try:
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert False
        except:
            assert True

    def test_can_pushed_higher_errors_and_blocked_in_outer_one(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
            print('Внешний блок: выполнено без ошибок')
            assert True
        except:
            assert False

    def test_can_ignored_child_errors(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert True
        except:
            assert False
