class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 考虑needle > haystack的情况
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        # 其他情况
        # 滑动窗口
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1