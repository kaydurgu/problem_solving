class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        used = [False] * len(isConnected)
        ans = 0
        def solve(x):
            used[x] = True
            for i in range(len(isConnected[x])):
                if isConnected[x][i] and not used[i]:
                    solve(i)
        for i in range(len(used)):
            if not used[i]:
                ans+=1
                solve(i)    
        return ans 