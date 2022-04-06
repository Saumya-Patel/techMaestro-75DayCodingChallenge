class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        op =[]
        nums.sort()
        if n<3:
            return []
        for i in range(0,n-2):
            a = i+1
            b = n-1
            while(a<b):
                sum = nums[a] + nums[b]
                if sum == -(nums[i]):
                    if [nums[i],nums[a], nums[b]] not in op:
                        op.append([nums[i],nums[a], nums[b]])
                    a = a+1
                    b = b-1
                elif sum> -(nums[i]):
                    b = b-1
                elif sum < -(nums[i]):   
                    a = a+1
        return op
