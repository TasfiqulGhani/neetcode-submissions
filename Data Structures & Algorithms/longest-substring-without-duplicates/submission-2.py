class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        unique = set()
        for R in range(len(s)):
            while s[R] in unique:
                unique.remove(s[L])
                L+=1
            else:
                unique.add(s[R]) 
            res = max(res, R - L +1)
        return res
