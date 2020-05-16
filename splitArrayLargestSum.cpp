#include <iostream>
#include <vector>
using namespace std;

// Split Array Largest Sum


/*
 Given an array which consists of non-negative integers and an integer m,
 you can split the array into m non-empty continuous subarrays.
 Write an algorithm to minimize the largest sum among these m subarrays.

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18
 */

/*
Explanation:

Let's define f[i][j] to be the minimum largest subarray sum for splitting nums[0..i] into j parts.

Consider the jth subarray. We can split the array from a smaller index k to i to form it. Thus f[i][j] can be derived from max(f[k][j - 1], nums[k + 1] + ... + nums[i]). For all valid index k, f[i][j] should choose the minimum value of the above formula.

The final answer should be f[n][m], where n is the size of the array.

For corner situations, all the invalid f[i][j] should be assigned with INFINITY, and f[0][0] should be initialized with 0.
 */


int splitArray(vector<int>& nums, int m) {
    // build dp
    int len = nums.size();
    vector<vector<int>>dp_array(len + 1, vector<int>(m, INT_MAX));
    dp_array[0][0] = nums[0];
    for (int i = 1; i < len; i++) {
        dp_array[i][0] = nums[i] + dp_array[i - 1][0];
    }

    for (int i = 0; i < len; i++) {
        for (int j = 1; j < m && j <= i; j++) {
            for (int k = 0; k < i; k++) {
                int curr_target = max(dp_array[k][j - 1], dp_array[i][0] - dp_array[k][0]);
                dp_array[i][j] = min(dp_array[i][j], curr_target);
            }
        }
    }
    return dp_array[len-1][m - 1];
}

/*
Time complexity : O(n^2∗m)
*/

int main() {
    vector<int>arr;
    arr.push_back(1);
    arr.push_back(INT_MAX);
    cout << splitArray(arr, 2) <<endl;
}