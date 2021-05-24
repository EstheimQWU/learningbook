class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # 准备双指针
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1