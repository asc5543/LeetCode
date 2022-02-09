class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #Dictionary to record the diff number
        dictDiff = {}
        intPair = 0
        for num in nums:
            # num+k or num-k
            if dictDiff.get(num):
                dictDiff[num] += 1
            else:
                dictDiff[num] = 1
        for key in dictDiff:
            if dictDiff.get(key+k) and (k != 0 or dictDiff[key]>1):
                intPair += 1
        return intPair
        
        