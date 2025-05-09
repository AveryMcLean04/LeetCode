class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 1 or len(x) == 0:
            return True
        elif x[0] != x[len(x) - 1]:
            return False
        else:
            return self.isPalindrome(x[1:(len(x) - 1)])
        