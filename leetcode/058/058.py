class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        l = s.split(' ')
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])