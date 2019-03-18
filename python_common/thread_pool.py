from threading import Thread
from Queue import Queue

class ThreadPool(object):

	def __init__(self, size):
		self._running = True
		self._queue = Queue()
		self._pool = []
		for i in xrange(size):
			self._pool.append(Thread(target=self._run, args=(i,)))
		for t in self._pool:
			t.start()

	def _run(self, tid):
		while True:
			func, args, kwargs = self._queue.get()
			if not self._running:
				return
			try:
				func(*args, **kwargs)
			except:
				print 'thread_pool_exception|tid=%s,func=%s,args=%s,kwargs=%s' % (tid, func.__name__, str(args), str(kwargs))
			finally:
				self._queue.task_done()

	def add_task(self, func, args=(), kwargs=None):
		if not self._running:
			raise RuntimeError('cannot add task to stopped pool')
		if kwargs is None:
			kwargs = {}
		self._queue.put((func, args, kwargs))

	def join(self):
		"""
		Blocks until all tasks in queue are processed
		"""
		self._queue.join()

	def stop(self):
		"""
		Terminates all threads in pool
		"""
		self._running = False
		for _ in self._pool:
			self._queue.put((None, None, None))
		for t in self._pool:
			t.join()

	def join_and_stop(self):
		self.join()
		self.stop()


def foo(x):
	print x

if __name__ == '__main__':
	thread_pool = ThreadPool(4)
	thread_pool.add_task(func=foo, args=(1,))
	thread_pool.add_task(func=foo, args=(2,))
	thread_pool.join()
