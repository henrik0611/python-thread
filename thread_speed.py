import threading
from utils import log_elapsed_time

N = 1000000
L = [0 for _ in range(N)]


def increase(l, start, stop, value=1):
	for i in range(start, stop):
		l[i] += value


@log_elapsed_time
def single_thread():
	print 'Single thread solution'
	global L
	increase(L, 0, N)


@log_elapsed_time
def multi_thread():
	print 'Multi thread solution'
	global L
	n_thread = 4
	item_per_thread = N / n_thread + N % n_thread
	threads = []
	for i in range(n_thread):
		first_item = i * item_per_thread
		last_item = min((i + 1) * item_per_thread, N)
		t = threading.Thread(target=increase, args=(L, first_item, last_item))
		t.start()
		threads.append(t)

	for thread in threads:
		thread.join()

if __name__ == '__main__':
	single_thread()
	print '\n'
	multi_thread()
