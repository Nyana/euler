#!/path/to/python
import time
print "Hello, Nyana, #9"


def find_prob9():
	for a in xrange(1, 1000):
		for b in xrange(a, 1000):
			c = 1000 - a - b
			if c > 0:
				if c*c == a*a + b*b:
					return a*b*c

tStart = time.time()
print find_prob9()
print "run time = " + str((time.time() - tStart))