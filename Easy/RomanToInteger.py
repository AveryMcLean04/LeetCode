class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        for i in range(n):
            if s[i] == 'I':
                if i + 1 < n and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    result += -1
                else:
                    result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                if i + 1 < n and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    result += -10
                else:
                    result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                if i + 1 < n and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    result += -100
                else:
                    result += 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
        return result
        