class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-1*k:]
        i = len(nums)-1
        while i - k >= 0:
            nums[i] = nums[i-k]
            i -= 1
        for i in range(len(temp)):
            nums[i] = temp[i]