class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map = set(nums)
        result = 0
        for n in nums:
            if n-1 not in map:
                l = 1
                while (n+l) in map:
                    l+=1
                result = max(result,l)
        return result
                

        