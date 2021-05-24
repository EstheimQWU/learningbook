class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        if strs == []:
            return ''
        len_of_strs = len(min(strs, key=len))
        # 获取最短位数，然后放进set中看是否长度为1
        for i in range(len_of_strs):
            public_set = set()
            # 循环放
            for item in strs:
                public_set.add(item[i])
            # 判断set长度是否为1
            if len(public_set) == 1:
                count += 1
                continue
            else:
                break
        return min(strs, key=len)[:count]
