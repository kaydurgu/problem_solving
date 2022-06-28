class Solution:
    def minDeletions(self, s: str) -> int:
        mp = collections.defaultdict(int)
        cnter = collections.Counter(s)
        lower = string.ascii_lowercase
        cnter = dict(sorted(cnter.items(),key = lambda item: item[1]))
        nakaz = []
        for key, val in cnter.items():
            if mp[val]:
                nakaz.append(val)
            else:
                mp[val]+=1
        arr = [0]
        for idx in range(1, 10 ** 5):
            if not mp[idx]:
                arr.append(idx)
        cnt = 0
        for i in nakaz:
            x = arr[bisect.bisect_left(arr, i) - 1]
            if x == 0:
                cnt += i
            else:
                arr.remove(x)
                cnt += (i - x)
        return cnt