row = 3
grid = range(1, row*row+1)

def getrow (grid=grid):
    count = 0
    while count < row:
        yield grid[row * count:row * (count + 1)]
        count += 1
    return

def getcol (grid=grid):
    count = 0
    while count < row:
        yield grid[count::row]
        count += 1
    return

def getdiag (grid=grid):
    count = 2
    i = 0
    while count:
        yield [x[i] for x in grid[::row]]
        count -= 1
        i = 0
    return

try:
    print "Rows:"
    rows = getrow()
    while 1:
        print "\t%s" % str(rows.next())
except:
    pass

try:
    print "Columns:"
    cols = getcol()
    while 1:
        print "\t%s" % str(cols.next())
except:
    pass

try:
    print "Diagonals:"
    diag = getdiag()
    while 1:
        print "\t%s" % str(diags.next())
except:
    pass
