class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0; q = 1; r = 1
        for i in range(n-1):
            p = q
            q = r
            r = p + q
        return r