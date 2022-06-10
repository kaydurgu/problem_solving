class Solution:
    def decodeString(self, s: str) -> str:
        def solve(s):
            letter, digit, multi, cnt = '', '', '', 0
            for i in range(len(s)):
                if not cnt:
                    if s[i].isalpha():
                        letter+=s[i]
                    if s[i].isdigit():
                        digit+=s[i]
                if s[i] in ['[', ']']:
                    if s[i] == '[':
                        cnt+=1
                    else:
                        cnt-=1
                    if not cnt:
                        return letter + int(digit) * solve(multi[1:]) + solve(s[i + 1:])
                if cnt > 0:
                    multi+=s[i]
            return letter
        return (solve(s))