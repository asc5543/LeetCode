class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        indexNonZero = 0
        for i in range(len(nums)):
            if not nums[i] == 0:
                tmp = nums[indexNonZero]
                nums[indexNonZero] = nums[i]
                nums[i] = tmp
                indexNonZero += 1

        
    # [0,1,0,3,12] -> [1,0,0,3,12]-> [1,3,0,0,12] -> [1,3,12,0,0]
    # [0] -> [0]
    # [1] -> [1]