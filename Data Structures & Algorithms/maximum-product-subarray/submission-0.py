class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nMin,nMax = 1,1
        res = max(nums)

        for n in nums:
            if n==0:
                nMin,nMax = 1,1
                continue 

            tmp = nMax*n
            nMax = max(nMax*n, n*nMin, n)
            nMin = min(tmp, n*nMin, n)
            res = max(nMax,res)
        return res

        