class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    # 在前一位插入
                    nums.insert(i-1, target)
                    return i
        return len(nums)