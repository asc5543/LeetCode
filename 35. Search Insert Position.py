class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        intLeft = 0
        intRight = len(nums)-1
        intMid = (intLeft + intRight) // 2
        while True:
            print intLeft, intRight, intMid
            if nums[intMid] == target:
                return intMid
            
            # index < target, find right
            elif nums[intMid] < target:
                # The biggest value or The next one larger than target, return index+1
                if intMid == len(nums)-1 or nums[intMid+1] > target:
                    return intMid+1
                
                # Otherwise, intLeft = intMid+1
                intLeft = intMid+1
                
            # index > target, find left
            elif nums[intMid] > target:
                # The smallest value, return it
                if intMid == 0:
                    return intMid
                
                # Otherwise, intRight = intMid
                intRight = intMid
                
            intMid = (intLeft + intRight) // 2
                
        return intMid