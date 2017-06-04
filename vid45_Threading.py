"""
Parallel programming (threading)

https://www.youtube.com/watch?v=NwH0HvMI4EA&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=45
"""

import threading
from queue import Queue
import time

# a special lock on any print function
print_lock = threading.Lock()

# an example job that takes a certain amount of itme
def exampleJob(worker):
    time.sleep(0.5)

    # syaing with that lock, print information
    with print_lock:
        print(threading.current_thread().name, worker)

# the core function of
def threader():
    while True:
        # empty the queue for each worker
        worker = q.get()
        # give that worker a job
        exampleJob(worker)
        # once they are done, release that thread
        q.task_done()


q = Queue()

# creates 10 workers
for x in range(10):
    # t is the worker, and the target is to go through threader
    t = threading.Thread(target=threader)
    # means that it works in the background
    t.daemon = True
    t.start()

# starting time
start = time.time()


for worker in range(20):
    q.put(worker)

# wait until the thread terminates
q.join()

print('Entire job took:', time.time() - start)
