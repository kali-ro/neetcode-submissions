class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r >= row or c >= col:
                return 0
            if (r, c) not in cache:
                down = dfs(r + 1, c)
                right = dfs(r, c + 1)
                diagonal = dfs(r + 1, c + 1)
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diagonal)
            return cache[(r, c)]

        dfs(0, 0)
        return max(cache.values()) ** 2

