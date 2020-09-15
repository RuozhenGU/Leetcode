
/*
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5


N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer; therefore

N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i,
 which implies that as long as N - (i - 1) * i / 2 is k times of i, 
 we get a solution corresponding to i; Hence iteration of all possible values of i, starting from 1, will cover all cases of the problem.
*/




class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int count = 1;
        for( int k = 2; k < sqrt( 2 * N ); k++ ) {
            if ( ( N - ( k * ( k - 1 )/2) ) % k == 0) count++;
        }
        return count;
    }
};