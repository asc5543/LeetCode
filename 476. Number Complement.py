class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        strBin = format(num, "b")
        intComp = 0
        for s in strBin:
            if s == "0":
                intComp = intComp*2 + 1
            else:
                intComp = intComp*2
        return intComp
    
    # 0 -> 1
    # 5 -> 101 -> 2
    