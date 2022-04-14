class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		res = {0: 1}
		pSum = 0
		c = 0
		for i in range(len(nums)):
			pSum = (pSum + nums[i]) % k
			if pSum < 0:
				pSum += k
			if pSum in res:
				c += res[pSum]
			if pSum not in res:
				res[pSum] = 0
			res[pSum] += 1
		return c
        
        
