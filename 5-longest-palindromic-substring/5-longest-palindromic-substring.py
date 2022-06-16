class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(left, right):
            if right == len(s):
                return s[left]
            if s[left] != s[right]:
                return s[left]
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            left = left + 1
            right = right - 1
            return  (s[left:right + 1])
                
        n = len(s)
        mx = 0
        for i in range(n):
            odd = solve(i, i)
            even = solve(i , i + 1)
            if len(odd) > mx:
                mx = len(odd)
                ans = odd
            if len(even) > mx:
                mx = len(even)
                ans = even 
        return ans 