def longest_increasing_subsequence(input_array):
    # array = [i for i in input_array]
    #
    # array.append(10 ** 5)
    # array.append(10 ** 5)
    # array.append(10 ** 5)
    # x, y, z = array[0], array[1], array[2]
    # longest_subseq = []
    #
    # for idx, e in enumerate(input_array):
    #     if max(x, y, z) != x and x not in longest_subseq and x != 10 ** 5:
    #         if longest_subseq == [] or longest_subseq[-1] < x:
    #             longest_subseq.append(x)
    #
    #     x, y, z = y, z, array[idx + 3]
    longest_subseq = {0:[]}

    for i in input_array:
        for array in sorted(longest_subseq):
            a = longest_subseq[array]
            if a and a[-1] < i:
                break
        longest_subseq[array - 1] = a + [i]
    return longest_subseq[min(longest_subseq)]




if __name__ == '__main__':
    print longest_increasing_subsequence([5, 19, 5, 81, 50, 28, 29, 1, 83, 23])