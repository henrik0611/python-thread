from threading import Thread
from Queue import Queue

from utils import log_elapsed_time
from matrix import Matrix

class MultiplicationWorker(Thread):
	def __init__(self, queue, result):
		super(MultiplicationWorker, self).__init__()
		self.queue = queue
		self.result = result

	def run(self):
		while True:
			row, col, a, b = self.queue.get()
			try:
				self.result[row][col] = dot_product(a, b)
			finally:
				self.queue.task_done()

def dot_product(a, b):
	n = len(a)
	result = 0
	for i in range(len(a)):
		result += a[i] * b[i]
	return result

@log_elapsed_time()
def naive_matrix_multiplication(mat_a, mat_b):
	if mat_a.c != mat_b.r:
		raise Exception('Invalid matrix size!')
	M, N, P = mat_a.r, mat_a.c, mat_b.c

	result_mat = []
	for i in xrange(M):
		row = []
		for j in xrange(P):
			vector_a = mat_a.get_row(i)
			vector_b = mat_b.get_col(j)
			row.append(dot_product(vector_a, vector_b))
		result_mat.append(row)
	return Matrix(M, P, result_mat)


@log_elapsed_time()
def multithreading_matrix_multiplication(mat_a, mat_b):
	if mat_a.c != mat_b.r:
		raise Exception('Invalid matrix size!')

	N_THREAD = 4
	M, N, P = mat_a.r, mat_a.c, mat_b.c
	result_mat = [[0 for _ in xrange(P)] for _ in xrange(M)]

	# Start workers
	queue = Queue()
	for _ in xrange(N_THREAD):
		worker = MultiplicationWorker(queue, result_mat)
		worker.daemon = True
		worker.start()

	# Add tasks
	for i in xrange(M):
		for j in xrange(P):
			queue.put((i, j, mat_a.get_row(i), mat_b.get_col(j)))

	queue.join()
	return Matrix(M, P, result_mat)


if __name__ == '__main__':
	M, N, P = 200, 200, 200
	A = Matrix(M, N)
	B = Matrix(N, P)

	naive_matrix_multiplication(A, B)
	multithreading_matrix_multiplication(A, B)