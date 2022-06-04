class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mx = 0
        used = [False] * len(arr)
        def Tuura(A :set, B: set):
            return len(A.union(B)) == len(A) + len(B)
        def solve(A,start):
            nonlocal mx
            mx = max(mx ,len(A))
            for i in range(start + 1, len(arr)):
                if not used[i] and Tuura(A, set(arr[i])) and len(set(arr[i])) == len(arr[i]):
                    B = set(arr[i])
                    used[i] = True
                    A = A.union(B)
                    solve(A, i)
                    A.difference_update(B)
                    used[i] = False
        solve(set(), -1)
        return mx