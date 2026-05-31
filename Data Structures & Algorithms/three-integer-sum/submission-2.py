class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            if a>0:
                break
            if i > 0 and nums[i-1]==nums[i]:
                continue

            left,right = i+1,len(nums)-1
            while left < right:
                sum = nums[left] + a + nums[right]

                if sum < 0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    result.append([nums[left] , a , nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left <right:
                        left+=1
                    
        return result