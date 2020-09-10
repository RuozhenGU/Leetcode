"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""




class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        process = []
        lst = list(s)

        for idx, s in enumerate(lst):
            
            if s == '[':
                stack.append(idx)
            if s == ']':
                process.append((stack.pop(), idx))
                
        for idx, item in enumerate(process):
            l, r = item
            # parse
            num_str = ''
            digit_count = 0
            
            for _i in range(l-1, -1, -1):
                if lst[_i].isdigit():
                    num_str = lst[_i] + num_str
                    digit_count += 1
                else:
                    break
                    
            repeat = int(num_str)

            decode = lst[l+1: r] * repeat

            # mask all encode part to ''
            for i in range(l-digit_count, r+1):
                lst[i] = ''
                
            lst[l-digit_count] = ''.join(decode) # very important, make changes first does not affect index since you are working on list
            
        
        # remove all empty string
        str_new = ''.join(lst)
        
        
        return str_new