class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)/2):
            tmp = s[i]
            s[i] = s[-1*(i+1)]
            s[-1*(i+1)] = tmp