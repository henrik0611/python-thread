import threading
import utils

THREAD_COUNT = 10
INC_COUNT = 100

value = 0
lock = threading.Lock()

def inc(n):
	global value
	for _ in range(n):
		with lock:
			value += 1

for i in range(THREAD_COUNT):
	t = threading.Thread(target=inc, args=(INC_COUNT,))
	t.start()

utils.join_other_threads()

print 'Actual: %s' % value
print 'Expected: %s' % (THREAD_COUNT * INC_COUNT)