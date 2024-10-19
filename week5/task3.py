"""
https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        flag1 = 0
        flag2 = 0

        for i in range(m):
            if matrix[0][i] == 0:
                flag1 = 1

        for i in range(n):
            if matrix[i][0] == 0:
                flag2 = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag1:
            for i in range(m):
                matrix[0][i] = 0

        if flag2:
            for i in range(n):
                matrix[i][0] = 0
