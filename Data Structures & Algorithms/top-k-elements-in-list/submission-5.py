class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i], 0)
        
        bucket = [ [] for _ in range(len(nums) + 1) ]

        for value, count in map.items():
              bucket[count].append(value)

        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                  result.append(item)
                  if len(result) == k:
                        return result
        return []
        