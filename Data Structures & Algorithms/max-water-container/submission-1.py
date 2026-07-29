class Solution:
    def maxArea(self, heights: List[int]) -> int:
      L = 0
      R = len(heights) - 1
      result = -1
      while L < R:
            result = max(result,  min(heights[L], heights[R]) * ( R - L ))
            if heights[L] < heights[R]:
                  L+=1
            else:
                  R-=1
      return result