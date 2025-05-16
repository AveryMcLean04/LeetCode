class Solution(object):
    def isValid(self, s):
        open = []
        for ch in s:
            if ch in "({[":
                open.append(ch)
            elif ch == ')' and open and open[-1] == '(':
                open.pop()
            elif ch == ']' and open and open[-1] == '[':
                open.pop()
            elif ch == '}' and open and open[-1] == '{':
                open.pop()
            else:
                return False
        return not open
