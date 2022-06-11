class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        used = [False] * n
        self.cable = 0  
        
        self.connected_components = 0
        
        mp = defaultdict(list)
        
        def solve(x):
            used[x] = True
            for y in mp[x]:
                if not used[y]:
                    solve(y)
                
        for x in connections:
            mp[x[0]].append(x[1])
            mp[x[1]].append(x[0])
        for i in range(len(used)):
            if not used[i]:
                self.connected_components+=1
                solve(i)
        
        if len(connections) < n - 1: 
            return -1
        return self.connected_components - 1
                    
            