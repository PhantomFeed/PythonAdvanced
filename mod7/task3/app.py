import sys
from utils import *
from FilterByLevel import *


logger = logging.getLogger('AppLogger')
logger.addHandler(FilterByLevel(mode='a'))


def main():
    x = input("Введите первое число: ")
    operator = input("Выберите операцию (+, -, *, /): ")
    y = input("Введите второе число: ")

    if validate_num(x):
        x = float(x)
        logger.info(f"{x} - корректное число")
    else:
        logger.error(f"{x} - некорректное число")
        return
    if validate_num(y):
        y = float(y)
        logger.info(f"{y} - корректное число")
    else:
        logger.error(f"{y} - некорректное число")
        return

    logger.info(f"Выполнение операции {operator} для {x} и {y}")

    try:
        if operator == '+':
            result = sum(x, y)
        elif operator == '-':
            result = subtract(x, y)
        elif operator == '*':
            result = multiply(x, y)
        elif operator == '/':
            result = divide(x, y)
        logger.info(f"Результат: {result}")
    except ValueError as e:
        logger.error(e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format='%(levelname)s | %(name)s | %(asctime)s | %('
                                                                       'lineno)d | %(message)s')
    main()
