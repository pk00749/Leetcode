from pythonds.basic.queue import Queue
import random

class Task:
    def __init__(self, current_time):
        self.timestamp = current_time
        self.pages = random.randrange(1, 21)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages


class Printer:
    def __init__(self, page_rate):
        self.page_rate = page_rate
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def next_task(self, task):
        self.current_task = task
        self.time_remaining = task.get_pages() * 60 / self.page_rate


def printer_simulator(num_sec, pages_per_min):
    printer = Printer(pages_per_min)
    wait_time_list = []
    print_queue = Queue()

    for sec in range(num_sec):
        if new_task():
            task = Task(sec)
            print_queue.enqueue(task)

        if (not printer.is_busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            wait_time_list.append(sec - next_task.get_timestamp())
            printer.next_task(next_task)

        printer.tick()

    average_wait_time = sum(wait_time_list) / len(wait_time_list)
    print('average: {aver}; waiting task: {tasks}'.format(aver=average_wait_time, tasks=print_queue.size()))


def new_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    printer_simulator(3600, 10)
