"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        ans = []

        def backtrack(string_builder, curr_idx):
            nonlocal S, ans

            if curr_idx == len(S):
                ans.append(string_builder)
                return

            character = S[curr_idx]

            for i in ["upper", "lower"]:  # upper & lower

                if not S[curr_idx].isalpha():
                    c = character
                elif i == "upper":
                    c = character.upper()
                else:
                    c = character.lower()

                tmp = string_builder[:]

                string_builder += c
                curr_idx += 1

                backtrack(string_builder, curr_idx)

                string_builder = tmp

                curr_idx -= 1

                if not c.isalpha():
                    break  # fucking important to remove duplcates in result. number only iterate once

        backtrack("", 0)

        return ans
