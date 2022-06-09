class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dp = defaultdict(int)
        inex = defaultdict(int)
        for i in range(len(numbers)):
            if dp[target - numbers[i]] > 0:
                return [inex[target - numbers[i]], i + 1]
            inex[numbers[i]] = i + 1
            dp[numbers[i]]+=1
        