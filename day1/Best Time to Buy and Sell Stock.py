class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        prof = 0 
        if len(prices) ==1:
            return 0
        else:
            for i in range(1,len(prices)):
                prof = max(prices[i]-mini,prof)
                mini =  min(prices[i],mini)
                    
        return prof
    
