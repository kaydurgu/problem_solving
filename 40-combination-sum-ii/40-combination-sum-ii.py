class Solution: 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used = [False] * len(candidates)
        mp = defaultdict(int)
        ans = []
        def solve(nums , remain, index):
            if remain == 0:
                ans.append(nums[::])
                return 
            for next_cur in range(index, len(candidates)):
                if next_cur > index and candidates[next_cur] == candidates[next_cur - 1]:
                    continue
                pick = candidates[next_cur]
                if remain - pick < 0:
                    break
                nums.append(pick)
                solve(nums, remain - pick, next_cur + 1)
                nums.pop()
        candidates.sort()
        solve([] , target, 0)
        return ans 