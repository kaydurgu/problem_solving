class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ones = deque()
        ans = [[math.inf] * len(grid) for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans[i][j] = 0
                    ones.append((i, j))
        dist = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        if not ones or len(ones) == (len(grid[0]) * len(grid)):
            return -1
        while ones:
            x, y = ones.popleft() 
            #print (x, y, ans)
            for i in range(4):
                new_x, new_y = x + dist[i][0], y + dist[i][1]
                if all([new_x >=0,
                        new_y >=0,
                        new_x < len(grid),
                        new_y < len(grid[0])]):
                    if ans[new_x][new_y] > ans[x][y] + 1:
                        ans[new_x][new_y] = ans[x][y] + 1
                        ones.append([new_x, new_y])
        return max([max(i) for i in ans])
                