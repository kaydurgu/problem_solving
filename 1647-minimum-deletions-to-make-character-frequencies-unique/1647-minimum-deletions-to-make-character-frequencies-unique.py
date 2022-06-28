class Solution:
    def minDeletions(self, s: str) -> int:
        mp = collections.defaultdict(int)
        cnter = collections.Counter(s)
        nakaz = []
        for key, val in cnter.items():
            if mp[val]:
                nakaz.append(val)
            else:
                mp[val]+=1
        arr, cnt = [0], 0
        for idx in range(1, 10 ** 5):
            if not mp[idx]:
                arr.append(idx)
        for i in nakaz:
            x = arr[bisect.bisect_left(arr, i) - 1]
            cnt += (i - x)
            if x != 0:
                arr.remove(x)
        return cnt