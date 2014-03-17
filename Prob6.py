#!/path/to/python
import time
print "Hello, Nyana, #6"


def find_prob6(n):
   found = False
   nb = 0
   nb2 = 0
   for i in range(n+1):
      nb += i*i

   for j in range(n+1):
      nb2 += j

   return (nb2*nb2)-nb

tStart = time.time()
print find_prob6(100)
print "run time = " + str((time.time() - tStart))