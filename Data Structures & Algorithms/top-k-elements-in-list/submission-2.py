class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
 
        for n, f in count.items():
            # [[1],[2],[3][][][]]
            freq[f].append(n)
        result = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


        
