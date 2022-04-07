class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans=0
		psum=0
		d={0:1}

		for i in nums:
			psum = psum + i

			if psum-k in d:
				ans = ans + d[psum-k]

			if psum not in d:
				d[psum] = 1
			else:
				d[psum] = d[psum]+1
