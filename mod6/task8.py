import re


def my_t9(digits):
    numword_dic = {
        '2': '[abc]',
        '3': '[def]',
        '4': '[ghi]',
        '5': '[jkl]',
        '6': '[mno]',
        '7': '[pqrs]',
        '8': '[tuv]',
        '9': '[wxyz]'
    }

    with open('/usr/share/dict/words', encoding='utf-8') as f:
        words = f.read().splitlines()

    digit_to_word = ''.join([numword_dic[digit] for digit in digits])
    res = re.compile(digit_to_word)
    result = [word for word in words if res.fullmatch(word)]

    return result


if __name__ == '__main__':
    words = my_t9(input())
    print(words)
