import logging
from logging import config
import logging_tree
from dictConfig import *


def logging_tree_to_txt(file):
    with open(file, 'w') as book:
        book.write(logging_tree.format.build_description())


logger = logging.getLogger('UtilsLogger')
logging.config.dictConfig(dict_config)

def validate_num(num):
    try:
        float(num)
        logger.info(f"{num} - корректное число")
        logger.info('You can see me!')
        logger.info('А меня нет')
        return True
    except ValueError:
        logger.error(f"{num} - некорректное число")
        return False


def sum(x, y):
    logger.info(f"Сумма {x} и {y}")
    return x + y


def subtract(x, y):
    logger.info(f"Вичтание {y} из {x}")
    return x - y


def multiply(x, y):
    logger.info(f"Умножение {x} на {y}")
    return x * y


def divide(x, y):
    if y == 0:
        logger.error("Делить на ноль нельзя")
        raise ValueError("Делить на ноль нельзя")
    logger.info(f"Деление {x} на {y}")
    return x / y


logging_tree_to_txt('logging_tree.txt')
