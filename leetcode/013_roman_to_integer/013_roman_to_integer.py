class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            # 判断本位是否是最后一位
            if i == len(s) - 1:
                # 是最后一位
                # 直接加法运算
                result = result + trans[s[i]]
            else:
                # 不是最后一位
                # 判断本位与下一位的大小
                if trans[s[i]] >= trans[s[i+1]]:
                    result = result + trans[s[i]]
                else:
                    result = result - trans[s[i]]
        return result

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

# 链接：https://leetcode-cn.com/problems/roman-to-integer/solution/2-xing-python-on-by-knifezhu/
"""
