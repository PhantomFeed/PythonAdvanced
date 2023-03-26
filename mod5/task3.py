import sys
sys.tracebacklimit = 0


class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True if(type in self.err_types or Exception in self.err_types or self.err_types in BaseException) \
            else False


if __name__ == '__main__' :
    err_types = {ZeroDivisionError, TypeError}
    with BlockErrors(err_types):
        a = 1 / 0
    print('Выполнено без ошибок')