class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        res = 0
        i = -1
        for j, c in enumerate(s):
            count[c] += 1
            while (j - i) - max(count.values()) > k:
                i += 1
                count[s[i]] -= 1
            res = max(res, j - i)
        return res
