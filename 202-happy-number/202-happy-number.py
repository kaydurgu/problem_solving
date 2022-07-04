class Solution:
    def isHappy(self, n: int) -> bool:
        used = {}
        while n>1:
            ans = 0
            for i in str(n):
                ans = ans + int(i)**2
            n = ans
            if (n in used):
                return False
            used[n] = 1
        return True