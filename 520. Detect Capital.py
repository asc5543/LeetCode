class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        """
        Only Three rule:
        1. All capital
        2. All not
        3. Only First
        """
        if len(word) < 2:
            return True
        intRule = -1
        if word[0].isupper():
            if word[1].isupper():
                intRule = 1
            else:
                intRule = 3
        else:
            intRule = 2
        for i in range(1, len(word)):
            if intRule == 1:
                if word[i].islower():
                    return False
            else:
                if word[i].isupper():
                    return False
        return True
    
    # "USA" -> True
    # "leetcode" -> True
    # "Google" -> True
    # "FlaG" -> False