class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        num_set = set(nums)
        max_val = 0
        for n in nums:
            if n-1 not in num_set:
                l = 0
                while n+l in num_set:
                    l+=1
                max_val = max(max_val,l)
        return max_val
 
                

        