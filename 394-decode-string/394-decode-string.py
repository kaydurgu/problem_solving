class Solution:
    def decodeString(self, s: str) -> str:
        def solve(s):
            letter = ''
            digit = ''
            multi = ''
            cnt = 0
            for i in range(len(s)):
                if cnt == 0:
                    if s[i].isalpha():
                        letter+=s[i]
                    if s[i].isdigit():
                        digit+=s[i]
                if s[i] in ['[', ']']:
                    if s[i] == '[':
                        cnt+=1
                        if cnt == 1:
                            continue
                    else:
                        cnt-=1
                    if cnt == 0:
                        #print(letter, digit , multi,s[i + 1:])
                        return letter + int(digit) * solve(multi) + solve(s[i + 1:])
                if cnt > 0:
                    multi+=s[i]
            return letter
        return (solve(s))