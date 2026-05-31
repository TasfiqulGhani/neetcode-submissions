class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #  [1,2,-3,4]
        min_r = 1
        max_r = 1
        result =   nums[0]
        for n in nums:
            temp = max_r
            max_r = max(n,max_r*n,min_r*n)
            min_r = min(n,temp*n,min_r*n)
            result = max(result,max_r)
        return result
    
        