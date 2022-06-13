class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        mp = defaultdict(list)
        
        used = [False] * n
        
        self.ans = 0
        
        def solve(x):
            used[x] = True
            for y, road in mp[x]:
                if not used[y]:
                    self.ans+=road
                    solve(y)
        
        for x, y in connections:
            mp[x].append([y, 1])
            mp[y].append([x, 0])
        
        solve(0)
        
        return (self.ans)