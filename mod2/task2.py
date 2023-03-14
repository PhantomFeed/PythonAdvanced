import sys


def get_mean_size(lines):
    files = len(lines)
    if files == 0:
        exit('Нет файлов')
    size = sum([int(x.split()[4]) for x in lines])
    return size / files


if __name__ == '__main__':
    print(get_mean_size(sys.stdin.readlines()[1:]))
