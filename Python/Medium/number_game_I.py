from fractions import gcd
from math import sqrt
def numbergameI(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    if a % 2 == 0 and b % 2 == 0:
        while a % 2 == 0:
            a = a / 2
        while b % 2 == 0:
            b = b / 2
    return a*b/gcd(a, b) - a - b \
        if a*b/gcd(a, b) - a - b > 0 \
        else - 1

def test(a, b):
    t = a*b/gcd(a, b) - a - b
    x = t/a
    y = t/b
    m = 0
    n = 0
    pairs = [(i, j) for i in xrange(x + 1) for j in xrange(y + 1)] + \
            [(i, j) for i in xrange(x + 1, -1 , -1) for j in xrange(y + 1, -1 ,-1)] + \
            [(i, j) for i in xrange(x + 1) for j in xrange(y + 1, -1 ,-1)] + \
            [(i, j) for i in xrange(x + 1, -1, -1) for j in xrange(y + 1)]

    for pair in pairs:
        if pair[0]*a + pair[1]*b == t:
            return pair

    return (-1, -1)

if __name__ == '__main__':

    print numbergameI(2, 3)
    print numbergameI(7, 9)
    print numbergameI(11, 3)
    print numbergameI(0, 16383)
    print numbergameI(16383, 0)
    print numbergameI(16383, 1)
    print numbergameI(16383, 16383)
    print numbergameI(883, 138) # passed
    print numbergameI(814, 504) # -1 failed
    print numbergameI(46, 445) # passed
    print numbergameI(168, 148) # -1 failed
    print numbergameI(118, 204) # -1 failed
    print numbergameI(778, 259) # passed
    print numbergameI(428, 482) # -1 failed
    print numbergameI(227, 612) # 138085 passed
    print numbergameI(515, 946) # 485729 passed
    print numbergameI(554, 167) # 91797 passed
    # print 883*138/gcd(883, 138)
    # print 12185
    # print 515*946/gcd(515, 946)
    #print numbergameI(883, 138) # 120833


