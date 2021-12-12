class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Question: How to check it can be partitioned into two subsets?
        # sum(nums) should be even, and largest num is not bigger than sum(nums)/2
        intSum = sum(nums)
        intTarget = intSum // 2
        if not intSum % 2 == 0:
            return False
        
        # Create list to record possible sum
        listDP = [False] * (intTarget+1) 
        listDP[0] = True # 0 is possible
        
        for num in nums:
            for i in range(intTarget, num-1, -1):
                # if listDP[i-num] == True, it means listDP[i] can be True
                # if listDP[i] == True, it meas listDP[i] is already possible 
                listDP[i] = listDP[i] or listDP[i-num]
        
        return listDP[intTarget]