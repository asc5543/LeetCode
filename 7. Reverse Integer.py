class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        intReverse = 0
        
        # Consider x > 0 first
        if x > 0:
            while not x == 0:
                if intReverse * 10 + x % 10 < 2**31:
                    intReverse = intReverse * 10 + x % 10
                    x = x // 10
                else:
                    return 0
        elif x < 0:
            if not x == (-1) * 2 ** 31:
                x = (-1) * x
            else:
                return 0
            while not x == 0:
                if intReverse * 10 + x % 10 < 2**31:
                    intReverse = intReverse * 10 + x % 10
                    x = x // 10
                elif intReverse * 10 + x % 10 == 2**31:
                    intReverse = (-1) * 2 ** 31
                else:
                    return 0
            intReverse = intReverse * (-1)
            
        return intReverse
    
    # 0 -> 0
    # 120 -> 21
    # -120 -> -21