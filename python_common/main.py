from threading import Thread
import asynctask
from thread_pool import ThreadPool

def foo(x):
	if x == 3:
		raise Exception('More than 2 but less than 4?')
	print x

if __name__ == '__main__':
	try:
		t = Thread(target=foo, args=(3,))
		t.start()
		t.join()
	except Exception as e:
		print e.message