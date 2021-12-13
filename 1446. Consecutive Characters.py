class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Record Result
        intPower = 0
        curChar = s[0]
        intTempPower = 0
        for i in range(len(s)):
            if s[i] == curChar:
                intTempPower += 1
            else:
                if intPower < intTempPower:
                    intPower = intTempPower
                intTempPower = 1
                curChar = s[i]
        if intPower < intTempPower:
            intPower = intTempPower
        return intPower
    
    # leetcode -> 2
    # eeeeee -> 6