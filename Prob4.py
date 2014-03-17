#!/path/to/python
import time
print "Hello, Nyana, #4"


def find_palind(n):
   largest_result_nb = n
   palind = 0
   while palind == 0 : 
      if is_palind(largest_result_nb):
         if find_palind_divisor(largest_result_nb) == 1:
            palind = 1
            return largest_result_nb
         else:
            largest_result_nb -= 1
      else:
         largest_result_nb -= 1

   print largest_result_nb


def is_palind(n):
   str_tmp = str(n)

   if str_tmp == str_tmp[::-1]:
      return True
   else : 
      return False

def find_palind_divisor(n):
   smallest_nb = 100
   largest_nb = 999
   palind = 0
   for i in range(smallest_nb, largest_nb):
      if n%i == 0 and len(str(n/i))<=3:
         palind = 1
         print i 
         print str(n/i)
         break
   return palind

tStart = time.time()
print find_palind(999999)
print "run time = " + str((time.time() - tStart))

