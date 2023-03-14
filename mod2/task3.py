import sys


def decoder(line):
    result = []
    for i in line:
        result.append(i)
        if len(result) > 2 and result[-1] == '.' and result[-2] == '.':
            del result[-3:]
    return ''.join(i for i in result if i != '.')


if __name__ == '__main__':
    print(decoder(sys.stdin.readline()))
