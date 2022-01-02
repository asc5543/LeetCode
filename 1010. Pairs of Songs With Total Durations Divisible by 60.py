class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dictComp = {}
        intPair = 0
        for duration in time:
            # Check has pair divisible by 60
            remainTime = duration % 60
            if dictComp.has_key(remainTime):
                intPair += dictComp[remainTime]
                
            # Set Comp into dictionary
            intComp = (60-remainTime) % 60
            if dictComp.has_key(intComp):
                dictComp[intComp] += 1
            else:
                dictComp[intComp] = 1
            
        return intPair
    
