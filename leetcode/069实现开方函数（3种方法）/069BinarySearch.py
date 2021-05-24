class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = -1
        while l <= r:
            # 怎么确定找到的是10不是11呢
            m = (l + r) // 2
            if m ** 2 == x:
                return int(m)
            elif m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                res = m
                l = m + 1
        return int(res)