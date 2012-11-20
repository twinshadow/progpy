print """
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

sumsqr = 0
sqrsum = 0
diff   = 0

for i in xrange (1, 101):
    sumsqr += i ** 2
    sqrsum += i

sqrsum = sqrsum ** 2

if sumsqr > sqrsum: diff = (sumsqr - sqrsum)
else              : diff = (sqrsum - sumsqr)

print "Difference: " + str (diff)
