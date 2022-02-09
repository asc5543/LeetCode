class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        indexLeft = 0
        indexRight = len(nums)-1
        while indexLeft < indexRight:
            indexMid = (indexLeft+indexRight)/2
            if nums[indexMid] < target:
                indexLeft = indexMid+1
            elif nums[indexMid] > target:
                indexRight = indexMid-1
            else:
                return indexMid
        if nums[indexLeft] == target:
            return indexLeft
        return -1