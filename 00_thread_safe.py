import threading
import utils

THREAD_COUNT = 10
INC_COUNT = 1000

value = 0

def inc(n):
	global value
	for _ in range(n):
		value += 1


for i in range(THREAD_COUNT):
	t = threading.Thread(target=inc, args=(INC_COUNT,))
	t.start()

utils.join_other_threads()

print 'Actual: %s' % value
print 'Expected: %s' % (THREAD_COUNT * INC_COUNT)
