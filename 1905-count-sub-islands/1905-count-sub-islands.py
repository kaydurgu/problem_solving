class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:    
        n, m = len(grid1), len(grid1[0])
        def solve(x, y):
            if any([x < 0, y < 0, x > (n - 1), y > (m - 1)]):
                return True
            if not grid2[x][y]:
                return True
            if grid2[x][y] != grid1[x][y]:
                return False
            grid2[x][y] = 0 
            return all([solve(x + 1, y), solve(x - 1,y), solve(x, y + 1), solve(x, y - 1)])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]:
                    ans+=solve(i, j)
        return ans 