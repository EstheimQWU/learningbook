class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 准备一个字典，检索为空则加入，不空则跳过，然后返回字典长度
        d = dict()
        for item in nums:
            if d.get(item, '') == item:
                # 删掉
                nums.remove(item)
                continue
            else:
                d[item] = item
        # 修改
        return len(d)