class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        suffix_seen = {}
        suffix_seen[0] = 0
        cur_sum = 0
        for idx ,val in enumerate(reversed(nums), 1):
            cur_sum += val
            suffix_seen[cur_sum] = idx
        cur_sum = 0
        mn = math.inf
        if x in suffix_seen:
            mn = min(mn, suffix_seen[x])
        for idx, val in enumerate(nums, 1):
            cur_sum += val
            need = x - cur_sum
            if need in suffix_seen:
                mn = min(mn, suffix_seen[need] + idx)
        if mn == math.inf:
            return -1
        return mn 