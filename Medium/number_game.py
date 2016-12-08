import numpy, pandas, unicodecsv

def number_game(number, n):
    def backtracking(number, subset, x, j):
        n = ''.join([str(number[i]) for i in xrange(len(number)) if subset[i] == 1])
        if n == '' or int(n) <= 1:
            return x
        else:
            if x == 1:
                return 0
            if int(n) % x == 0:
                # check if current number can be divided by x
                res = x
                for i in xrange(len(number) - 1, -1, -1):
                    if i != j and subset[i] == 1:
                        subset[i] = 0
                        value = backtracking(number, subset, x - 1, i)
                        subset[i] = 1
                        if value < res:
                            res = value
                return res
            else:
                return x

    subset = [1 for i in xrange(len(number))]

    res = n
    for i in xrange(len(number) - 1, -1, -1):
        subset[i] = 0
        value = backtracking(number, subset, n, i)
        subset[i] = 1
        if value < res:
            res = value
    return n - res


def main():
    # print number_game("102045", 4)
    # print number_game("5555", 3)
    print number_game("88", 2)
    print number_game("912056", 3)
    print number_game("912056", 5)
    print number_game("112046", 7)
    print number_game("503012", 15)
    print number_game("833010", 15)
    print number_game("233010", 15)
    print number_game("100000", 4)
    print number_game("123456", 6)

if __name__ == '__main__':
    main()