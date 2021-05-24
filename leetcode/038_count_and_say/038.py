class Solution:
    def countAndSay(self, n: int) -> str:
        # 递归
        if n == 1:
            return n
        else:
            source = countAndSay(n-1)
            res = ""
            # 1个1
            for item in source:
                res = res + int(item) + item
            return int(res)