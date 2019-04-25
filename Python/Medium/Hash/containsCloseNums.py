def containsCloseNums(nums, k):
    if len(nums) < 2:
        return False
    distance_list = {}

    for idx, i in enumerate(nums):
        if i not in distance_list:
            distance_list[i] = [idx]
            continue
        if i in distance_list:
            distance_list[i].append(idx)

    result = {}

    for key, values in distance_list.items():
        if len(values) > 1:
            distance = []
            for idx in range(len(values) - 1):
                distance.append(values[idx+1] - values[idx])
            result[key] = distance

    for key, values in result.items():
        d = list(filter(lambda x: x <= k, values))
        if d != []:
            return True
    return False

if __name__ == '__main__':
    # nums = [0,1,2,3,5,2]
    # k = 3
    # nums = [0, 1, 2, 3, 5, 2]
    # k = 2
    # nums = [99, 99]
    # k = 2/3
    nums = [1,2]
    k = 2
    nums = [1, 2, 1]
    k = 2

    print(containsCloseNums(nums, k))

