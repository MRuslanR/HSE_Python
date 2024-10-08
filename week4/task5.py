"""
https://leetcode.com/problems/rotate-image/description/
"""


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = (
                    matrix[n - j - 1][n - i - 1],
                    matrix[i][j],
                )
                print(matrix[i][j], matrix[n - j - 1][n - i - 1])

        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        return matrix
