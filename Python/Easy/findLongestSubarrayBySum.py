def findLongestSubarrayBySum(s, arr):
    prefix_sum = [0]
    
    if len(arr) < 2:
        return [1,1] if arr[0] == s else [-1]

    for idx, i in enumerate(arr):
        prefix_sum.append(i + prefix_sum[idx])

    left_pointer = 1
    right_pointer = 2
    current_length = 0
    current_pos = []
    print prefix_sum
    
    while right_pointer < len(prefix_sum):
        if prefix_sum[left_pointer] + s >= prefix_sum[right_pointer]:
            right_pointer += 1
        elif prefix_sum[left_pointer] + s < prefix_sum[right_pointer]:
            if prefix_sum[left_pointer] + s == prefix_sum[right_pointer - 1]:
                if current_length < right_pointer - left_pointer:
                    current_length = right_pointer - left_pointer
                    current_pos = [left_pointer + 1, right_pointer - 1]
            left_pointer = right_pointer
            right_pointer += 1

    return current_pos



if __name__ == '__main__':
    # print findLongestSubarrayBySum(468, [135, 101, 170, 125, 79, 159, 163, 65, 106, 
    # 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 
    # 154, 93, 183, 22, 117, 119, 96, 48, 127, 0, 172, 0, 139, 0, 0, 
    # 70, 113, 68, 100, 36, 95, 104, 12, 123, 134])
    #print findLongestSubarrayBySum(12,[1,2,3,7,5])
    print findLongestSubarrayBySum(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])