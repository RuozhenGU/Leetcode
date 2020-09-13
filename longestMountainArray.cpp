
/*
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
*/

/* 
donot use dp
use two ptr technique.  a mountain can only start after the previous one ends.

*/


class Solution {
public:
    int longestMountain(vector<int>& A) {
        
        if (A.size() == 0 || A.size() == 1) return 0;
        
        int start = 0;
        int end = 1;
        int ans = 0;
        
        while (start < A.size() -1) {
            end = start + 1;                // so important ! without -> infinite loop
            //detect the start of a mountain
            if (end < A.size() && A[end-1] < A[end]) {
                // find peak
                while (end < A.size() && A[end - 1] < A[end]) {
                    end++;
                }
                // verify if this is actually a mountain
                if (end < A.size() && A[end - 1] > A[end]) {
                    
                    while (end < A.size() && A[end - 1] > A[end]) {
                        end++;
                    }
                    
                    // save soln
                    if (end - start + 1 > ans) ans = end - start;
                    start = end - 1;
                } else {
                    start = end;
                }
                
            } else {
                // no mountain
                start = end;
            }
        }
        return ans;
    }
};