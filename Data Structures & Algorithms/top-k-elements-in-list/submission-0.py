class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        result = []
        frq = [[] for i in range(len(nums)+1)] 
        for n in nums:
            count[n] = count.get(n,0) +1

        for n , c in count.items():
            frq[c].append(n)
            
        for i in range(len(frq)-1, 0 , -1):
            for n in frq[i]:
                result.append(n)
                if len(result) == k:
                    return result