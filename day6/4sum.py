class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        nums = sorted(nums)
        
        for k in range(len(nums)):
            for i in range(k+1, len(nums)):
                left = i+1
                right = len(nums) - 1
                while left < right:
                    sum = nums[k] + nums[i] + nums[left] + nums[right]
                    if sum > target:
                        right -=1
                    elif sum < target:
                        left +=1
                    else:
                        val = [nums[k], nums[i], nums[left], nums[right]]
                        if val not in op:
                            op.append(val)
                        left +=1
                        while nums[left] == nums[left-1] and left < right:
                            left +=1
                            
        return op
        
