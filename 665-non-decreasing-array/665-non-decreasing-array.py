class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fir, sec = nums[:], nums[:]
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                fir[i - 1] = nums[i]
                sec[i] = nums[i - 1] 
                break
        return sorted(fir) == fir or sorted(sec) == sec