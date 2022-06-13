class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        mp = defaultdict(list)
        road = defaultdict(dict)
        for x, y in connections:
            road[x][y] = 1
        used = [False] * n
        self.ans = 0
        def solve(x):
            used[x] = True
            for y in mp[x]:
                if not used[y]:
                    if road.get(x, False):
                        if road.get(x).get(y, False):
                            self.ans+=1
                    solve(y)
        for x, y in connections:
            mp[x].append(y)
            mp[y].append(x)
        solve(0)
        return (self.ans)