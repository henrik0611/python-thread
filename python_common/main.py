import logging
from threading import Thread
import asynctask
from thread_pool import ThreadPool

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(threadName)s|%(message)s',)

def foo(x):
	if x == 3:
		raise Exception('More than 2 but less than 4?')
	logging.info(x)

if __name__ == '__main__':
	thread_pool = ThreadPool(4)
	for i in xrange(100):
		thread_pool.add_task(func=foo, args=(i, ))
	thread_pool.join_and_stop()