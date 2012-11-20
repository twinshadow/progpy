print """
Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

list = xrange(1, 1000)
total = 0

for i in list:
    if i % 5 is 0 or \
       i % 3 is 0 :
        total += i 

print "Answer: " + str (total)
