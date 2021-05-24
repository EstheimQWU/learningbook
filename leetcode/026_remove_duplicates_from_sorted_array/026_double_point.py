class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	# i为慢指针，j为快指针
    	if nums == []:
    		return 0
    	i = 0
        for j in range(len(nums)):
        	if nums[i] != nums[j]:
        		i = i + 1
        		nums[i] = nums[j]
        return i + 1   # 相差1
