import logging

logger = logging.getLogger('UtilsLogger')

def validate_num(num):
    try:
        float(num)
        logger.info(f"{num} - корректное число")
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