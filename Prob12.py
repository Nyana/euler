#!/path/to/python
import time
import prime
print "Hello, #12"


 for i in xrange(1, 1000000000):
     n = i * (i+1) / 2
     if prime.num_factors(n) > 500:
         print n
         break