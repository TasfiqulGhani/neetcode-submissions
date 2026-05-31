class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
            rob1, rob2 = 0, 0 
            for n in nums:
                tmp = max(rob1+n,rob2)
                rob1 = rob2
                rob2= tmp
            return rob2