class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for n in nums:
            map[n] = 1 + map.get(n, 0)

        freq = [ [] for _ in range(len(nums)+1)]
        for key, count in map.items():
            freq[count].append(key)
        result = []
        for i in range(len(freq)-1,-1,-1):
            for x in freq[i]:
                result.append(x)
                if len(result) == k:
                    return result





        
