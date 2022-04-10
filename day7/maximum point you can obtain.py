class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
	    k = len(cardPoints) - k
	    total = sum(cardPoints)
	    minpoints = ksum = sum(cardPoints[:k])
	    for i in range(k, len(cardPoints)):
		    ksum += cardPoints[i] - cardPoints[i-k]
		    minpoints = min(minpoints, ksum)
	    return total - minpoints
