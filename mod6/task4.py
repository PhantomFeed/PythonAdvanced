import itertools
import json
import operator
from collections import Counter


def read_book(filename: str) -> list[dict]:
    with open(filename) as book:
        logs = [json.loads(log) for log in book]
    return logs


logs = read_book('skillbox_json_messages.log')


def group_by_level(logs):
    logs_list = Counter(log['level'] for log in logs)
    for level, count in logs_list.items():
        print(f'{level}: {count}')


def group_by_time(logs):
    time_list = {}
    for time, logs_list in itertools.groupby(sorted(logs, key=lambda d: d['time']), key=lambda d: d['time'][0:2]):
        time_list[time] = len(list(logs_list))
    max_hour, max_count = max(time_list.items(), key=operator.itemgetter(1))
    print(f'Больше всего логов ({max_count}шт) было в {max_hour} часов')


def group_by_time_in_current_period(logs, level):
    result = [log for log in logs if (log.get('level') == level and '05:00' <= log.get('time', '') < '05:20')]
    print(f'Логов уровня {level} в период с 05:00 по 05:20 было: {len(result)}')


def group_by_word(logs, word):
    filtered_data = [log.get("message") for log in logs if word.lower() in (log.get("message") or "").lower()]
    count = len(filtered_data)
    print(f'Количество сообщений, содержащих слово "{word}": {count}')


def group_by_most_common_word(logs, level):
    filtered_logs = [log for log in logs if log.get('level') == level]
    words_list = " ".join([log['message'] for log in filtered_logs]).split()
    word, count = Counter(words_list).most_common()[0]
    print(f'Слово, которое встречается чаще всего в сообщениях уровня {level}: "{word}", встречалось {count} раз')


if __name__ == '__main__':
    group_by_level(logs)
    group_by_time(logs)
    group_by_time_in_current_period(logs, 'CRITICAL')
    group_by_word(logs, 'dog')
    group_by_most_common_word(logs, "WARNING")
