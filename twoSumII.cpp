/*
question: same as 2 sum but now the array is sorted
*/

/*
explain:

We use two indexes, initially pointing to the first and last element respectively.
 Compare the sum of these two elements with target. If the sum is equal to target, we found the exactly only solution.
  If it is less than target, we increase the smaller index by one. If it is greater than target, we decrease the larger index by one. 
  Move the indexes and repeat the comparison until the solution is found.
*/


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0, high = numbers.size() - 1;
        while (low < high) {
            int sum = numbers[low] + numbers[high];
            if (sum == target)
                return {low + 1, high + 1};
            else if (sum < target)
                ++low;
            else
                --high;
        }
        return {-1, -1};
    }
};