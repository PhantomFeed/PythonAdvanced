import queue
import random
import threading
import time


class Task:

    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f'Task(priority={self.priority}).    sleep({random.random()})'


class Producer(threading.Thread):
    def __init__(self, queue: queue.PriorityQueue, count: int):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self):
        print('Producer: Running')
        for i in range(self.count):
            priority = random.randint(0, 6)
            task = Task(priority)
            self.queue.put((priority, task))
        consumer = Consumer(self.queue)
        consumer.start()
        consumer.join()
        print('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, queue: queue.PriorityQueue):
        super().__init__()
        self.queue = queue
        self.count = 0

    def run(self):
        print('Consumer: Running')
        while True:
            priority, task = self.queue.get()
            self.count += 1
            print(f'>running {task}')
            time.sleep(random.random())
            self.queue.task_done()
            if self.count == 10:
                print('Consumer: Done')
                break


def main():
    q = queue.PriorityQueue()
    producer = Producer(q, 10)
    producer.start()
    q.join()


if __name__ == '__main__':
    main()
