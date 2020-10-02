class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B[0])
        C = [[0]*n for _ in range(m)]
        for i_a in range(len(A)):
            for j_b in range(len(B[0])): # iterate over col of B
                for i_b in range(len(B)): # iterate over row of B
                    C[i_a][j_b] += A[i_a][i_b] * B[i_b][j_b]
        return C