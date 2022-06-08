class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        if len(s) == 0:
            return 0
        if s == s[::-1]:
            return 1
        return 2
        