class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(result) and j < len(strs[i]) and result[j] == strs[i][j]:
                j += 1
            result = result[:j]
            if result == "":
                return ""

        return result
