class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, arr, curr_sum):
            
            if curr_sum == target:
                result.append(arr.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return

            arr.append(candidates[i])
            dfs(i+1, arr, curr_sum + candidates[i])
            arr.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, arr, curr_sum)
        candidates.sort()
        dfs(0,[],0)
        return result



