class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        used = [False] * n
        
        self.connected_components = 0
        
        mp = defaultdict(set)
        
        def solve(x):
            used[x] = True
            for y in mp[x]:
                if not used[y]:
                    solve(y)
                
        for x in connections:
            mp[x[0]].add(x[1])
            mp[x[1]].add(x[0])
            
        for i in range(len(used)):
            if not used[i]:
                self.connected_components+=1
                solve(i)
        
        if len(connections) < n - 1: 
            return -1
        return self.connected_components - 1
                    
            