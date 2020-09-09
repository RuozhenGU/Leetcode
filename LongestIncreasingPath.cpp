/*
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 

You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
*/

class Solution {
public:

    int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; 

    int dfs(int i, int j, vector<vector<int>>& matrix, vector<vector<int>>& visited) {


        for(auto &ele : dir) {

            if ((ele[0] + i >= 0 && ele[0] + i <= matrix.size() - 1) &&
                (ele[1] + j >= 0 && ele[1] + j <= matrix[0].size() - 1)) {

                int x = i + ele[0];
                int y = j + ele[1];

                // make sure worth to continue
                if (matrix[x][y] < matrix[i][j]) {


                    // if x,y has been visited, we only need to find compare and find the max, no need to DFS
                    if (visited[x][y] != 1) {

                        visited[i][j] = max(visited[i][j], visited[x][y] + 1); // include or not include

                    } else { 
                        int ans = dfs(x, y, matrix, visited);
                        visited[i][j] = max(visited[i][j], ans + 1);
                    } 
                }
            }
        }
        return visited[i][j];
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        
        if (matrix.size() == 0) return 0;
        
        int max_len = 0;

        vector<vector<int>> visited;
                
        // 2d matrix filled in with 0
        for(int n = 0; n < matrix.size(); n++) {
            vector<int> tmp(matrix[0].size(), 1); // fill in 1 not 0
            visited.emplace_back(tmp);
        }
        
        
        for(int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {

                int ans;

                if (visited[i][j] != 1) ans = visited[i][j]; //dp process to cache pre-computed result
                else ans = dfs(i, j, matrix, visited); 
                
                max_len = max(max_len, ans);
            }
        }
        
        return max_len;
    }
};

// Time complexity : O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once.