
def rotateArray(a):
    p = []

    res = [[] for i in a]

    for j in xrange(len(a)-1, -1, -1):
        for k in xrange(len(a)):
            res[k].append(a[j][k])

    return res



if __name__ == '__main__':
    print rotateArray([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    print rotateArray([[1]]) == [[1]]



