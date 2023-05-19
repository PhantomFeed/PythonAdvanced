import logging
import multiprocessing
from multiprocessing.pool import Pool, ThreadPool
import requests
import sqlite3
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = f'https://swapi.dev/api/people/'


def create_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute('''CREATE TABLE
     IF NOT EXISTS characters 
     (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, age INTEGER)''')


insert_characters = """
INSERT INTO characters (name, gender, age) VALUES (?, ?, ?)
"""


# def get_characters():
#     start = time.time()
#     characters = []
#     for i in range(1, 20):
#         response = requests.get(URL + str(i))
#         if response.status_code == 200:
#             data = response.json()
#             name, gender, age = data['name'], data['gender'], data['birth_year'] if data['birth_year'] != 'unknown' else None
#             characters.append((name, gender, age))
#
#     cursor.executemany(insert_characters, characters)
#
#     logger.info('Done in {:.4}'.format(time.time() - start))


def get_character(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name, gender, age = data['name'], data['gender'], data['birth_year'] if data['birth_year'] != 'unknown' else None
        return name, gender, age


def get_characters_pool():
    pool = Pool(processes=multiprocessing.cpu_count())
    start = time.time()
    urls = [URL + str(i) for i in range(1, 22)]
    results = pool.map(get_character, urls)
    pool.close()
    pool.join()
    characters = [result for result in results if result is not None]
    cursor.executemany(insert_characters, characters)

    logger.info('Pool done in {:.4}'.format(time.time() - start))

def get_characters_threadpool():
    pool = ThreadPool(processes=multiprocessing.cpu_count() * 5)
    start = time.time()
    urls = [URL + str(i) for i in range(1, 22)]
    results = pool.map(get_character, urls)
    pool.close()
    pool.join()
    characters = [result for result in results if result is not None]
    cursor.executemany(insert_characters, characters)

    logger.info('ThreadPool done in {:.4}'.format(time.time() - start))


if __name__ == '__main__':
    with sqlite3.connect('star_wars.db') as db:
        cursor = db.cursor()
        create_table(cursor)
        get_characters_pool()
        get_characters_threadpool()
        db.commit()

    db.close()