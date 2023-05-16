import logging
import random
import threading
import time

TOTAL_TICKETS = 100
AVAILABLE_TICKETS = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super(Director, self).__init__()
        self.lock = semaphore
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS, AVAILABLE_TICKETS
        while TOTAL_TICKETS:
            if AVAILABLE_TICKETS == 4:
                with self.lock:
                    tickets_to_print = 10 - (AVAILABLE_TICKETS % 10)
                    if tickets_to_print > TOTAL_TICKETS:
                        tickets_to_print = TOTAL_TICKETS
                    AVAILABLE_TICKETS += tickets_to_print
                    TOTAL_TICKETS -= tickets_to_print
                    logger.info(f'Director printed {tickets_to_print} tickets. {TOTAL_TICKETS} tickets remaining')
        logger.info('Director stops work, not more tickets left.')


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS, AVAILABLE_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            if TOTAL_TICKETS != 0 and AVAILABLE_TICKETS == 4:
                continue
            else:
                if AVAILABLE_TICKETS == 0:
                    break
            with self.sem:
                AVAILABLE_TICKETS -= 1
                self.tickets_sold += 1
                logger.info(f'{self.name} sold one; {AVAILABLE_TICKETS} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 2))


def main():
    semaphore = threading.Semaphore()
    director = Director(semaphore=semaphore)
    director.start()
    sellers = [director]

    for i in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()
