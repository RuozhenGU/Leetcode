"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
"""

# 如果不用merge interval就得用array of same length as s，每个index标识是否当前这一位需要bold， 把end移动到俩loop外，
#  只要 i 小于 end就标识
# 最后加上去tag的时候，发现如果这一位有标识，就bold
class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        mark = []
        for i in range(len(s)):
            end = -1
            for item in dict:
                l = len(item)
                if l + i <= len(s):
                    if s[i: i+l] in dict:
                        end = max(end, i+l)
            if end != -1:
                mark.append([i, end])
            
        mark = self.merge(mark)
        mark = mark[:: -1]
        print(mark)
        for i, j in mark:
            s = s[0: i] + '<b>' + s[i: j] + '</b>' + s[j:]
            print(s)
        return s