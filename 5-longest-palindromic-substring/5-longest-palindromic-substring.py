class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            if left + 1 == right:
                return s[left]
            left = left + 1
            right = right - 1
            return  (s[left:right + 1])
        arr = []
        for i in range(len(s)):
            arr.append(solve(i, i))
            arr.append(solve(i , i + 1))
        return max(arr ,key = len)