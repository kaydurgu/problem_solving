class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([entrance])
        n ,m = len(maze) , len(maze[0])
        mn = math.inf
        dist = [[math.inf] * m for i in range(n)]
        dist[entrance[0]][entrance[1]] = 0
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            x, y = q.popleft()
            if any([x == (n - 1), x == 0, y == (m - 1), y == 0]) and [x , y] != entrance:
                mn = min(dist[x][y], mn)
            for i, j in moves:
                new_x, new_y = i + x, j + y
                if all([new_x < n, new_x >= 0, new_y < m, new_y >= 0]) and maze[new_x][new_y] == '.':
                    if dist[new_x][new_y] > dist[x][y] + 1:
                        dist[new_x][new_y] = dist[x][y] + 1
                        q.append([new_x, new_y])
        return mn if mn != math.inf else -1 
                    
        