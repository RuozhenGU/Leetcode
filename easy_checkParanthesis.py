class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lst = {'(':')', '{':'}','[': ']'}
        for i in range(len(s)):
            if s[i] in lst:
                stack.append(s[i])
            else:
                if stack == []: return False # important!
                ele = stack.pop()
                if lst[ele] == s[i]:
                    continue
                else:
                    return False
        return True if stack == [] else False # important