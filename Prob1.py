#!/path/to/python

print "Hello, World!"

i, answer = 0,0

while i <1000 :
   if (i%3 == 0) or (i%5 == 0):
      answer = answer + i

   i = i + 1

print answer
