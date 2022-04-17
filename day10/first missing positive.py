class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_ele = max(nums)
        set_num = set(nums)
        
        if max_ele < 1:
            return 1
        for i in range(1, max_ele+2):
            if i not in set_num:
                return i
