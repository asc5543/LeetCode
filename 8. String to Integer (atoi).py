class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        target = "+-0123456789"
        intReturn = 0
        boolNegtive = False
        boolSeem = False
        for c in s:
            if c in target:
                if c == '-':
                    if boolSeem:
                        break
                    boolNegtive = True
                    boolSeem = True
                elif c == '+':
                    if boolSeem:
                        break
                    boolNegtive = False
                    boolSeem = True
                else:
                    if not boolNegtive and intReturn*10+int(c) > 2**31-1:
                        return 2**31-1
                    if boolNegtive and intReturn*10+int(c) > 2**31:
                        return (-1) * 2**31
                    intReturn = intReturn*10+int(c)
                    boolSeem = True
            elif c == " " and not boolSeem:
                continue
            else:
                break
        if boolNegtive:
            intReturn = intReturn*(-1)
        return intReturn