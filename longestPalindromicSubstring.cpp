//
// Created by Gabriel Gu on 2020-05-16.
//


/*
 * Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    O(n^2)
 */

#include <iostream>
#include <vector>
using namespace std;

string longestPalindrome(string s) {
    int len = s.length();
    int result_range = INT_MIN;
    std::string result = s.substr(0, 1);

    //base case
    if (s.length() == 0) return "";
    if (s.length() == 1) return s;

    vector<vector<int> > f(len, vector<int>(len, 0));
    // base case: init f[i][i] and f[i][i+1]
    for(int i = 0; i < len; i++) {
        f[i][i] = 1;

        if (i + 1 < len && s[i] == s[i + 1]) {

            f[i][i + 1] = 1;

            result_range = 2;
            result = s.substr(i, 2);

        } else if (i + 1 < len) {
            f[i][i + 1] = 0;
        }
    }

    // fill in the rest of dp array from bottom to top
    for(int i = len - 1; i >= 0; i--) {
        for (int j = 0; j < len; j++) {
            if (i >= j || i == j + 1) continue; // not valid or already considered in bc
            if (f[i + 1][j - 1] && s[i] == s[j]) {
                f[i][j] = 1;
                if ((j - i + 1) > result_range) {
                    result_range = j - i + 1;
                    result = s.substr (i, j - i + 1);
                }
            }
        }
    }


    return result;
}

int main() {
    string s = "ac";
    cout << "result is " << longestPalindrome(s) <<endl;
}