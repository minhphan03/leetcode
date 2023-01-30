class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        DP = [[0 for i in range(n)] for j in range(m)]

        DP[0][0] = grid[0][0]

        for i in range(1,n):
            DP[0][i] = DP[0][i-1] + grid[0][i]
        for i in range(1,m):
            DP[i][0] = DP[i-1][0] + grid[i][0]
       
        for i in range(1, m):
            for j in range(1, n):
                up = DP[i-1][j] + grid[i][j]
                left = DP[i][j-1] + grid[i][j]
                DP[i][j] = up if up <= left else left
        return DP[m-1][n-1]
