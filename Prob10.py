#!/path/to/python
import time
print "Hello, #10"


def find_prob10(n):
	prime_array = []
	nb_tmp = 3
	prime_array.append(2)
	total = 0
	while nb_tmp <= n:
		prime = True
		for i in prime_array:
			if i*i < nb_tmp:
				if nb_tmp%i == 0:
					prime = False
					break
		if prime == True:
			prime_array.append(nb_tmp)
		nb_tmp += 1
	for j in prime_array:
		total += j

	return total


tStart = time.time()
print find_prob10(2000000)
print "run time = " + str((time.time() - tStart))