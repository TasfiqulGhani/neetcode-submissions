        
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False
        
        s1_map = Counter(s1)
        window = Counter(s2[:len_s1])

        if s1_map == window:
            return True 
        for i in range(len_s1, len_s2):
            window[s2[i]] +=1 
            window[s2[i-len_s1]] -=1  
            if s1_map == window:
                return True
        return False