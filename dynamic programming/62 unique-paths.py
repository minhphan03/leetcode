class Solution(object):
    def uniquePaths(self, m, n):
        DP = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            DP[i][0] = 1
        for i in range(n):
            DP[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[m-1][n-1]
       
