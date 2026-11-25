class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row
        l = 0
        r = len(matrix) - 1

        # col
        t = 0
        b = len(matrix[0]) - 1

        row = 0
        while (l <= r):
            row = (l + r) // 2
            if matrix[row][0] > target:
                r = row - 1
            elif matrix[row][-1] < target:
                l = row + 1
            else:
                break

        col = 0
        while (t <= b):
            col = (t + b) // 2
            if matrix[row][col] < target:
                t = col + 1
            elif matrix[row][col] > target:
                b = col - 1
            else:
                return True

        return False