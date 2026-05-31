class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 1 2 3
        # 1+(0)  1+(2)  1+(3)  1
        one,two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one