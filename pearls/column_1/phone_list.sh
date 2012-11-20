#!/bin/sh

# Generating the (very naieve) phone number list takes a while on slower
# computers and about 37Mb of disk space, compressed; 77Mb uncompressed.

python -c 'for n in xrange (1,10000000): print "{0:0>7}".format(n)' | \
shuf |\
gzip > phone_list2.gz
