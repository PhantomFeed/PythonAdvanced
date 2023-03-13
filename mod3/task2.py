import unittest
from mod2.task3 import decoder


class TestDecoderApp(unittest.TestCase):
    def test_with_one_point_in_task3(self):
        encrypted_words = ['абра-кадабра.', '.']
        correct_words = ['абра-кадабра', '']
        for i in (0, len(encrypted_words) - 1):
            with self.subTest(i=i):
                self.assertEqual(decoder(encrypted_words[i]), correct_words[i])

    def test_with_two_points_in_task3(self):
        encrypted_words = ['абраа..-кадабра', 'абра--..кадабра']
        correct_words = ['абра-кадабра', 'абра-кадабра']
        for i in (0, len(encrypted_words) - 1):
            with self.subTest(i=i):
                self.assertEqual(decoder(encrypted_words[i]), correct_words[i])

    def test_with_three_points_in_task3(self):
        encrypted_words = ['абраа..-.кадабра', 'абрау...-кадабра', '1..2.3']
        correct_words = ['абра-кадабра', 'абра-кадабра', '23']
        for i in (0, len(encrypted_words) - 1):
            with self.subTest(i=i):
                self.assertEqual(decoder(encrypted_words[i]), correct_words[i])

    def test_with_more_then_three_points_in_task3(self):
        encrypted_words = ['абра........', 'абр......a.', '1.......................']
        correct_words = ['', 'а', '']
        for i in (0, len(encrypted_words) - 1):
            with self.subTest(i=i):
                self.assertEqual(decoder(encrypted_words[i]), correct_words[i])
