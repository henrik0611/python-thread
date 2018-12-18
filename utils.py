import threading
import dis

def join_other_threads():
	main_thread = threading.currentThread()
	for t in threading.enumerate():
		if t is not main_thread:
			t.join()

def disassenble(func):
	dis.dis(func)