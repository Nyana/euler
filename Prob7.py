#!/path/to/python
import time
print "Hello, Nyana, #7"


def find_prob7(n):
	prime_array = []
	isprime = 1
	nb_tmp = 2
	prime_array.append(2)
	while len(prime_array) <= n-1:
		prime = True
		for i in prime_array:
			if nb_tmp%i == 0:
				prime = False
				break
		if prime == True:
			prime_array.append(nb_tmp)
		nb_tmp += 1

	return prime_array[len(prime_array)-1]

tStart = time.time()
print find_prob7(10001)
print "run time = " + str((time.time() - tStart))