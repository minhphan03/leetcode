class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for j in range(n)]
        start = 1

        self.spiral(0, n-1, 0, n-1, start, res)
        return res

    def spiral(self, row1, row2, col1, col2, start, matrix):
        if (row1 > row2) or (col1 > col2):
            return

        # add first row
        for i in range(col1, col2 + 1):
            matrix[row1][i] = start
            start +=1

        # add last column
        for i in range(row1 + 1, row2+1):
            matrix[i][col2] = start
            start +=1

        # add last row if last and first column is not the same
        if row1 != row2:
            for i in range(col2 - 1, col1 - 1, -1):
                matrix[row2][i] = start
                start +=1

        # add first column if last and first row is not the same
        if col1 != col2:
            for i in range(row2 - 1, row1, -1):
                matrix[i][col1] = start
                start +=1

        self.spiral(row1 + 1, row2 - 1, col1 + 1, col2 - 1, start, matrix)