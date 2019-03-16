import time
import random

random.seed(time.time())


class Matrix(object):
	LIMIT = 1000

	@classmethod
	def _get_random_list(cls, len):
		return [random.randint(1, cls.LIMIT) for _ in xrange(len)]

	def __init__(self, r, c, mat=None):
		self.r = r
		self.c = c

		if mat is None:
			self.mat = [self._get_random_list(c) for _ in xrange(r)]
		else:
			self.mat = mat
		self._create_transpose_mat()

	def __str__(self):
		return '\n'.join([str(self.get_row(i)) for i in xrange(self.r)])

	def _create_transpose_mat(self):
		self.t_mat = []
		for j in xrange(self.c):
			self.t_mat.append([self.mat[i][j] for i in xrange(self.r)])

	def get(self, i, j):
		return self.mat[i][j]

	def get_row(self, i):
		return self.mat[i]

	def get_col(self, i):
		return self.t_mat[i]