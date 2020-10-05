"""
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i, _s in enumerate(s):
            if _s == "(":
                stack.append((_s, i))
            if _s == ")":
                if stack == []:
                    remove.append(i)
                else:
                    stack.pop()
        for item in stack:
            remove.append(item[1])

        s = list(s)
        for idx in remove[::-1]:
            s.pop(idx)

        return "".join(s)
