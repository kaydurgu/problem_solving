class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def solve(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or not grid[x][y] :
                return 0
            grid[x][y] = 0
            return 1 + solve(x + 1, y) + solve(x - 1, y) + solve(x, y + 1)+ solve(x, y - 1)
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    mx = max(solve(i,j),mx)
        return mx 