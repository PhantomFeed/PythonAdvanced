import json
import logging
import getpass
import hashlib
import os
import re


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = json.dumps(msg, ensure_ascii=False)
        return msg, kwargs


logger = JsonAdapter(logging.getLogger('password_checker'))


with open("/usr/share/dict/words", "r") as f:
    words = f.read().splitlines()


def is_strong_password(password: str):
    logger.debug('Начало is_strong_password')
    for word in words:
        if word in password.lower() and len(word) > 4:
            return False
    return True


def input_and_check_password():
    logger.debug('Начало input_and_check_password')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы ввели пустой пароль.')
        return False

    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))

        if not is_strong_password(password):
            logger.warning('Пароль не является сложным')

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception('Вы ввели некорретный символ ', exc_info=ex)

    return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='skillbox_json_messages.log', format='{"time": "%(asctime)s", '
                                                                                          '"level": "%(levelname)s", '
                                                                                          '"message": %(message)s}',
                                                                                          datefmt="%H:%M:%S")
    logger.info('Вы пытаетесь аутентифицироваться в Skillbox')
    count_number: int = 3
    logger.info(f'У вас {count_number} попытки')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь трижды ввёл неправильный пароль!')
    exit(1)
