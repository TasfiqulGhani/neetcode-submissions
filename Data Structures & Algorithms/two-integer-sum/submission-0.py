import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        unique_numbers = {}
        for i, n in enumerate(nums):
            if target - n in unique_numbers:
                return [unique_numbers[target - n],i]
            else:
                unique_numbers[n]=i
        return -1


        