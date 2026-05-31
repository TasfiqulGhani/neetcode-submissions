class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique_values = set(nums)
        for n in unique_values:
            if (n-1) not in unique_values:
                lenth = 1
                while (n+lenth) in unique_values:
                    lenth+=1
                result = max(result,lenth)
        return result



        