class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def solve(x, y):
            if any([x > (len(grid) - 1) , x < 0, y < 0, y  > (len(grid[0]) - 1)]):
                return False
            if grid[x][y] == 1:
                return True
            grid[x][y] = 1
            return all([solve(x + 1, y),
                        solve(x - 1, y),
                        solve(x, y + 1),
                        solve(x, y - 1)])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    ans+=solve(i, j)
        return ans 
        