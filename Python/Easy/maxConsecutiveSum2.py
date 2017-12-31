def arrayMaxConsecutiveSum2(inputArray):
    prefix_sum = [0]  

    if list(filter(lambda x : x > 0 ,inputArray)) == []:
        return max(inputArray)

    for idx, i in enumerate(inputArray):
        prefix_sum.append(i + prefix_sum[idx])

    i = 0
    j = 0

    for idx in xrange(len(prefix_sum)):
        if prefix_sum[idx] >= i:
            i = prefix_sum[idx]
            j = idx 

    return i - min(prefix_sum[0:j])
if __name__ == '__main__':
    print arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6])
    print arrayMaxConsecutiveSum2([-3, -2, -1, -4])
    print arrayMaxConsecutiveSum2([-3, 2, 1, -4])
    print arrayMaxConsecutiveSum2([1, -2, 3, -4, 5, -3, 2, 2, 2])
    print arrayMaxConsecutiveSum2([11, -2, 1, -4, 5, -3, 2, 2, 2])
    rint arrayMaxConsecutiveSum2([89, 96, 60, 10, 24, 30, 72, 40, 74, 49, 38, 87, 55, 46, 44, 14, 49, 88, 93, 11])
        