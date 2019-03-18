import threading
import utils

N_THREAD = 10
INC_VALUE = 1000

value = 0

def inc(n):
	global value
	for _ in range(n):
		value += 1

if __name__ == '__main__':
	for i in range(N_THREAD):
		t = threading.Thread(target=inc, args=(INC_VALUE,))
		t.start()

	utils.join_other_threads()

	print 'Actual: %s' % value
	print 'Expected: %s' % (N_THREAD * INC_VALUE)