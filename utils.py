import threading
import dis
import time

def log_elapsed_time():
	def _log_elapsed_time(func):
		def _func(*args, **kwargs):
			start_time = time.time()
			result = func(*args, **kwargs)
			elapsed = time.time() - start_time
			print 'Run %s in %d ms' % (func.__name__, elapsed * 1000)
			return result
		return _func
	return _log_elapsed_time