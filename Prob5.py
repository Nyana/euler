#!/path/to/python
import time
print "Hello, Nyana, #5"


def find_prob5(n):
   value_range = n
   found = False
   nb = n

   while found == False:
      i = 1
      while i <= value_range and nb%i == 0:
         if i == value_range:
            found = True
            return nb
         i += 1
      nb += n

def is_divisible_range_x(n, nb):
   divisible = 1
   for i in range(n):
      if nb%i != 0:
         divisible = 0
         break
   return divisible


tStart = time.time()
print find_prob5(20)
print "run time = " + str((time.time() - tStart))

