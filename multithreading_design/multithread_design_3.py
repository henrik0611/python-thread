import threading
import logging
from threading import Thread
from Queue import Queue, Empty

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(threadName)s|%(message)s',)


class DaemonWorker(Thread):
	def __init__(self, task_queue):
		super(DaemonWorker, self).__init__()
		self.task_queue = task_queue

	def start(self):
		self.daemon = True
		super(DaemonWorker, self).start()

	def run(self):
		while True:
			try:
				task_name = self.task_queue.get()
				self._process(task_name)
			finally:
				self.task_queue.task_done()

	def _process(self, task_name):
		logging.info(task_name)

if __name__ == '__main__':
	TASKS = 10
	WORKERS = 4
	task_queue = Queue()

	# Start daemon workers
	for i in xrange(WORKERS):
		daemon_worker = DaemonWorker(task_queue)
		daemon_worker.start()

	# Add tasks
	for i in xrange(TASKS):
		task_queue.put("Task %s" % i)

	# Wait for all tasks to be done
	task_queue.join()

