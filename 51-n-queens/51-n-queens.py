class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def stav(grid, x, y, n ,queen, beated):
            for i in range(n):
                grid[x][i] += beated
            for i in range(n):
                grid[i][y] += beated
            for k in range(-n, n + 1):
                if k + x >= 0 and k + x < n and y - k < n and y - k >=0:
                    grid[k + x][y - k] += beated
                if k + x >=0 and k + x < n and 0 <= y + k and y + k < n:
                    grid[k + x][y + k] += beated            
            grid[x][y] = queen              
            return grid 
        
        def Tuura(row, column, grid):
            for i in range(row):
                for j in range(n):
                    if grid[i][j] == 'Q' and (column == j or 
                                              i+j == row+column or 
                                              i-j == row-column):     
                        return False
            return True
        def solve(row, grid, n):
            if row == n:
                ans.append([''.join(roww) for roww in grid])
                return 
            for i in range(n):
                if Tuura(row, i, grid):
                    grid[row][i] = 'Q'
                    solve(row + 1, grid, n)
                    grid[row][i] = '.'
        grid = [['.'] * n for j in range(n)]
        solve(0, grid, n)
        return ans 
        