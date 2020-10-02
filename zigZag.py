"""
    
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I



"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ["" for _ in range(numRows)]
        if numRows == 1:
            return s
        row_idx = 0
        col = -1
        for i in range(len(s)):
            if i % (numRows + numRows - 2) == 0:
                col += 1
                row_idx = 0
            elif (i - (col * (numRows + numRows - 2))) >= numRows:
                row_idx -= 1
            else:
                row_idx += 1

            ans[row_idx] += s[i]

        return "".join(ans)

        """
        another soln2

        Visit all characters in row 0 first, then row 1, then row 2, and so on...

        For all whole numbers kkk,

        Characters in row 000 are located at indexes k  (2⋅numRows−2)k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2)
        Characters in row numRows−1\text{numRows}-1numRows−1 are located at indexes k  (2⋅numRows−2)+numRows−1k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1
        Characters in inner row iii are located at indexes k  (2⋅numRows−2)+ik \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i and (k+1)(2⋅numRows−2)−i(k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i.

        """
