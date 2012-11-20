def bits (n):
    '''Represent an integer as an array of binary digits.'''

    bits = []
    while n > 0:
        n, bit = divmod (n, 2)
        bits.append (bit)

    bits.reverse()
    return bits

