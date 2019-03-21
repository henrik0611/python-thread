import threading
import utils

N_THREAD = 10
INC_VALUE = 1000

value = 0
lock = threading.Lock()

def inc(n):
	global value
	for _ in range(n):
		with lock:
			value += 1

if __name__ == '__main__':
	threads = []
	for i in range(N_THREAD):
		t = threading.Thread(target=inc, args=(INC_VALUE,))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()

	print 'Actual: %s' % value
	print 'Expected: %s' % (N_THREAD * INC_VALUE)