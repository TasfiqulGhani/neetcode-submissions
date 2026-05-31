class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        c = 0
        l = 0
        result = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r],0)
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]]-=1
                l+=1
            result = max(result, (r - l + 1) )
        
        return result

 
           



