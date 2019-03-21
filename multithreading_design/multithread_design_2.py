import threading
import logging
from threading import Thread
from Queue import Queue, Empty

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(threadName)s|%(message)s',)


class Worker(Thread):
	def __init__(self, task_queue):
		super(Worker, self).__init__()
		self.task_queue = task_queue

	def run(self):
		while True:
			try:
				task_name = self.task_queue.get(block=False)
				self._process(task_name)
			except Empty:
				break

	def _process(self, task_name):
		logging.info(task_name)


if __name__ == '__main__':
	TASKS = 10
	WORKERS = 4

	# Add tasks
	task_queue = Queue()
	for i in xrange(TASKS):
		task_queue.put("Task %s" % i)

	# Start workers
	workers = []
	for i in xrange(WORKERS):
		worker = Worker(task_queue)
		worker.start()
		workers.append(worker)

	# Wait for all workers to finish
	for worker in workers:
		worker.join()



