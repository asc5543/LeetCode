class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        dictComp = {}
        for i in range(len(nums)):
            if not nums[i] in dictComp.keys():
                dictComp[target-nums[i]] = i
            else:
                return [dictComp[nums[i]],i]