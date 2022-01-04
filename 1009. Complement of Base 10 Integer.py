class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        strBin = format(n, "b")
        intComp = 0
        for s in strBin:
            if s == "0":
                intComp = intComp*2 + 1
            else:
                intComp = intComp*2
        return intComp
    
    # 0 -> 1
    # 5 -> 101 -> 2
    