# exceed limit

class Solution(object):
    def uniquePaths(self, m, n):
        num = []
        x = 0
        y = 0
        def traverse(self, m, n, x, y, count):
            if x+1 == m and y+1 == n:
                count.append(1)
                return
            elif x == m or y == n:
                return
            traverse(m, n, x+1, y, count)
            traverse(m, n, x, y+1, count)
            return
        traverse(m, n, x+1, y, num)
        traverse(m, n, x, y+1, num)
        return len(num)
    
    def uniquePaths2(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths2(m-1, n) + self.uniquePaths2(m, n-1)
    
    # Arpit Choudhary on Medium
    def uniquePaths3(self, m, n):
        DP = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            DP[i][0] = 1
        for i in range(n):
            DP[0][i] = 0
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[m-1][n-1]


print(Solution().uniquePaths3(3, 7))
