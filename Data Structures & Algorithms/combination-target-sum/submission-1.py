class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, arr, curr_sum):
            
            if curr_sum == target:
                result.append(arr.copy())
                return
            
            if i >= len(nums) or curr_sum > target:
                return

            arr.append(nums[i])
            dfs(i, arr, curr_sum + nums[i])
            arr.pop()
            dfs(i+1, arr, curr_sum)
        dfs(0,[],0)
        return result



