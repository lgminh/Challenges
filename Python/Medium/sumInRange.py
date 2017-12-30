def sumInRange(nums, queries):
	prefix_sum = {0:0}
	t = 0	
	s = 0
	
	for idx, i in enumerate(nums):
		t += i
		prefix_sum[idx+1] = t

	print prefix_sum

	for query in queries:
		s += (prefix_sum[query[1] + 1] - prefix_sum[query[0]]) % (10**9 + 7)

	return s % (10**9+7)



if __name__ == '__main__':
	sumInRange([-25,-7,15,19,4,27,37,49,-10], [[2,3],[0,3],[0,0],[4,6]])
	