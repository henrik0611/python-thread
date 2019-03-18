import dis

value = 0
l = [4, 1, 3, 2]

def inc():
	global value
	value += 1

def sort():
	global l
	l.sort()

dis.dis(sort)