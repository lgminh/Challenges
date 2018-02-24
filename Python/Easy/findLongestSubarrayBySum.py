def findLongestSubarrayBySum(s, arr):
    prefix_sum = [0]
    
    if len(arr) < 2:
        return [1,1] if arr[0] == s else [-1]

    for idx, i in enumerate(arr):
        prefix_sum.append(i + prefix_sum[idx])
    current_length = 0
    current_pos = []

    left_pointer = 0
    right_pointer = 1
    previous_left = 0
    previous_right = 0

    while left_pointer < len(prefix_sum) - 1 or right_pointer < len(prefix_sum) - 1:
        previous_left = left_pointer
        previous_right = right_pointer
        if prefix_sum[right_pointer] - prefix_sum[left_pointer] <= s:
            if prefix_sum[right_pointer] - prefix_sum[left_pointer] == s:
                if current_length < right_pointer - left_pointer + 1:
                    current_length = right_pointer - left_pointer + 1
                    current_pos = [left_pointer + 1, right_pointer]
                if right_pointer == len(prefix_sum) - 1:
                    break
            if right_pointer < len(prefix_sum) - 1:
                right_pointer += 1
        else:
            left_pointer += 1

        if previous_right == right_pointer and previous_left == left_pointer:
            break

    return current_pos if current_pos != [] else [-1]



if __name__ == '__main__':
    print findLongestSubarrayBySum(468, [135, 101, 170, 125, 79, 159, 163, 65, 106,
    146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103,
    154, 93, 183, 22, 117, 119, 96, 48, 127, 0, 172, 0, 139, 0, 0,
    70, 113, 68, 100, 36, 95, 104, 12, 123, 134])
    print findLongestSubarrayBySum(12,[1,2,3,7,5])
    print findLongestSubarrayBySum(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print findLongestSubarrayBySum(3,[3])
    print findLongestSubarrayBySum(3,[2])
    print findLongestSubarrayBySum(665,  [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124,
                                      142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65,
                                      49, 47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24,
                                      85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124,
                                      138, 139, 119, 83, 130, 142, 34, 116, 40, 59, 105, 131,
                                      178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174, 98, 113])
    print findLongestSubarrayBySum(167, [101, 168, 93, 188, 133, 157, 175])
    print findLongestSubarrayBySum(15,[1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10])