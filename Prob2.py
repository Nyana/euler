#!/path/to/python

print "Hello, Nyana , #2"

i = 2
x,y = 1,2

while (y < 4000000) and (x < 4000000) :

   if x < y:
      x += y
      if x%2 == 0 :
         i += x
   else:
      y += x
      if y%2 == 0 :
         i += y

print i

