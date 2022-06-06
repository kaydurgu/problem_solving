class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def solve(x, y):
            if any ([x < 0, y < 0, x > (n - 1), y > (m - 1)]):
                return -math.inf
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return (1 + solve(x + 1, y) + solve(x - 1, y) + solve(x, y + 1) + solve(x, y - 1))
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    could = solve(i,j)
                    res+= could if could > 0 else 0
        return (res)
        