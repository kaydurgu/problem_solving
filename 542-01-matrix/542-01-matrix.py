class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        dist = [[math.inf] * len(mat[0]) for i in range (len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append([i, j])
        moves = [[-1 , 0], [1 , 0], [0, -1], [0, 1]]
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                new_x, new_y = x + moves[i][0], y + moves[i][1]
                if all([new_x >=0, new_y >=0, new_x < len(mat),new_y < len(mat[0])]):
                    if dist[new_x][new_y] > dist[x][y] + 1:
                        dist[new_x][new_y] = dist[x][y] + 1
                        queue.append([new_x, new_y])
                            
        return dist