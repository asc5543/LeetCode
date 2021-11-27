class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        intLeft=0
        intWhite = 0
        intBlue = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                nums[intLeft] = 0
                intLeft += 1
            elif nums[i] == 1:
                intWhite += 1

        for j in range(intLeft, intLeft+intWhite):
            nums[j] = 1
        for k in range(intLeft+intWhite, len(nums)):
            nums[k] = 2