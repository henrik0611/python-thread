import threading
import time
import logging
from threading import Thread

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(threadName)s|%(message)s',)

def process(task_name):
	logging.info(task_name)

if __name__ == '__main__':
	N_THREAD = 4
	threads = []
	for i in xrange(N_THREAD):
		task_name = 'Task %s' % i
		thread = Thread(target=process, args=(task_name, ))
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()
