class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        intMax = nums[0]
        Sum = nums[0]
        
        # Current continuous Min
        intMin = min(nums[0],0)
        for i in range(1, len(nums)):
            Sum = Sum + nums[i]
            
            # Sum is larger than current recorded max or Sum - continuous Min is larger than recorded Max
            if Sum > intMax or Sum - intMin > intMax:
                intMax = max(Sum, Sum - intMin)

                
            # Record current continuous Min
            if Sum < intMin:
                intMin = Sum
                
        return intMax