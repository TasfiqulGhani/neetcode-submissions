class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = []
        target = sum(nums)//2

        for i in range(len(nums)+1):
            dp.append([-1] * (target+1))


        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            
            if target < 0:
                return False
            if dp[i][target] != -1:
                return dp[i][target]

            dp[i][target] = dfs(i+1, target) or dfs(i+1, target - nums[i])
            return dp[i][target]
        
        return dfs(0, sum(nums)//2)

            
        