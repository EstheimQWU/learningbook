class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 克隆
        nums1_copy = nums1[:m] 
        nums1[:] = []

        # 指针
        p1 = 0
        p2 = 0

        # 对比
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            elif nums1_copy[p1] > nums2[p2]:
                nums1.append(nums2[p2])
                p2 += 1
            elif nums1_copy[p1] == nums2[p2]:
                nums1.append(nums2[p2])
                p2 += 1

        # 处理空余字符
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]