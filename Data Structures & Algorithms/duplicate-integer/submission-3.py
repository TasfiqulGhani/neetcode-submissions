class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = []
        for n in nums:
            if n in maps:
                return True
            else:
                maps.append(n)
        return False
         