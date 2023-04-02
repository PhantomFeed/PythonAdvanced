import logging.config
from utils import *
from FilterByLevel import *
from dictConfig import dict_config

logger = logging.getLogger('AppLogger')
# format = '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
# formatter = logging.Formatter(format)
# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(formatter)
# custom_handler = FilterByLevel(mode='a')
# custom_handler.setFormatter(formatter)
# logging.basicConfig(level=logging.INFO, handlers=[handler, custom_handler])
logging.config.dictConfig(dict_config)


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
    main()
