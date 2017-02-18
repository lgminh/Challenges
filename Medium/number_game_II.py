def numbergameII(n):
    lose = 1
    r = 2

    while lose <= n:
        if lose == n:
            return False
        if lose + r >= 2 ** r:
            r += 1
        lose += r
    return True


if __name__ == '__main__':
    print numbergameII(1)
    print numbergameII(2)
    print numbergameII(4)
    print numbergameII(5)
    print numbergameII(6)
    print numbergameII(7)
    print numbergameII(8)
    print numbergameII(9)
    print numbergameII(10)
