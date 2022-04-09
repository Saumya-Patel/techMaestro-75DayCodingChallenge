class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pair = {}
        c = 0 
            
        for i in time:
            rem = i%60
            if (60-rem) in pair:
                c = c+ pair[(60-rem)]
            if rem == 0 and rem in pair:
                c = c+ pair[rem]
            if rem in pair:
                pair[rem] += 1
            else:
                pair[rem] = 1
        return c
