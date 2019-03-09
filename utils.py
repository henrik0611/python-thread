import threading
import dis
import time

def join_other_threads():
	main_thread = threading.currentThread()
	for t in threading.enumerate():
		if t is not main_thread:
			t.join()

def disassenble(func):
	dis.dis(func)

def log_elapsed_time(func):
	def _func(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		elapsed = time.time() - start_time
		print 'Elapsed time = %d ms' % (elapsed * 1000)
		return result
	return _func