class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        if len(s) == 0:
            return 0
        while left<=right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return 2
        return 1
        