class Solution:
    def valid(self,A):
        bal = 0
        for c in A:
            if c == '(': 
                bal += 1
            else: 
                bal -= 1
            if bal < 0: 
                return False
        return bal == 0
    def solution(self,s : str, length : str):
        if len(s) == length* 2:
            if self.valid(s):
                #print(s)
                self.ans.append(s)
        else:
            for i in range(1, 3):
                
                s += self.mp[i]
                self.solution(s, length)
                s = s[:len(s) - 1]
                
    def generateParenthesis(self, n: int) -> List[str]:
        self.mp = {1 : '(',
                   2 : ')'
                  }  
        self.ans = []
        res = []
        
        self.solution('' , n)
        
        return self.ans