"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def format_level(level, maxWidth, length, curr):

            # edge case: last line
            if curr == length:
                remain = maxWidth - len(" ".join(level))
                return " ".join(level) + " " * (remain)

            # edge case: 1 word only
            if len(level) == 1:
                return level[0] + " " * (maxWidth - len(level[0]))

            remain = maxWidth - len("".join(level))
            spaces_between, spaces_extra = divmod(remain, len(level) - 1)
            for i, item in enumerate(level):
                if spaces_extra == 0:
                    break
                level[i] += " "
                spaces_extra -= 1
            return (" " * spaces_between).join(level)

        curr = 0
        ans = []
        level = []
        remaining = maxWidth

        while curr < len(words):
            if remaining - len(words[curr]) >= 0:  # dont subtract extra 1
                remaining = remaining - len(words[curr]) - 1
                level.append(words[curr])
                curr += 1
            else:
                remaining = maxWidth
                ans.append(format_level(level, maxWidth, len(words), curr))
                level = []
        ans.append(format_level(level, maxWidth, len(words), curr))
        return ans
