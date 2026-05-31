class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_le=0
        map = set()
        for i in range(len(s)):
            while s[i] in map:
                map.remove(s[l])
                l+=1
            map.add(s[i])
            max_le=max(max_le, i-l+1)
        return max_le
        