class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        longest = 0
        map_set = set(nums) 
        for n in map_set:
            if n-1 not in map_set:
                l = 1
                while n +l in map_set:
                    longest = max(longest, l)
                    l+=1
        return longest + 1
        



