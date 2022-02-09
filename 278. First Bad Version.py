# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        intLeft = 1
        intRight = n
        while intLeft < intRight:
            intMid = (intLeft+intRight)/2
            # True, the first bad is appeared before this version
            if isBadVersion(intMid):
                intRight = intMid
            else:
                if isBadVersion(intMid+1):
                    return intMid+1
                intLeft = intMid
        # intLeft = intRight
        if isBadVersion(intLeft):
            return intLeft