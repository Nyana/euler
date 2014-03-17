#!/path/to/python
import time
print "Hello, Nyana, #3"

n = 600851475143

def find_factor(n):
   factor = []
   isprime = 1
   factor.append(2)
   for i in range(100000):
      if i*i < n :
         if i%2 == 1 and i > 1 and n%i == 0:
            for j in factor:
               if i%j == 0 and isprime == 1:
                  isprime = 0
            if isprime == 1:
               factor.append(i)
   if len(factor) <= 1:
      print "Prime number"
   else:
      print factor[len(factor)-1]
tStart = time.time()
find_factor(n)
print "run time = " + str((time.time() - tStart))

# tStart = time.time()
# n = 600851475143
# i = 2
# while i * i < n:
#     while n % i == 0:
#         n = n / i
#     i = i + 1
# print n
# print "run time = " + str((time.time() - tStart))