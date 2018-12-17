l = [1, 3, 2]

def foo():
	l.sort()

import dis
dis.dis(foo)