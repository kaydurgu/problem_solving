class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * (len(rooms))
        def solve(x):
            for room in rooms[x]:
                if not visited[room]:
                    visited[room] = True
                    solve(room)
        visited[0] = True
        solve(0)
        print (visited)
        return all(visited)