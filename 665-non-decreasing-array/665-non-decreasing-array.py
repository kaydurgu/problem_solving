class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        fir, sec = nums[:], nums[:]
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                fir[i - 1] = nums[i]
                sec[i] = nums[i - 1] 
                break
        print (sec)
        print (fir)
        if sorted(fir) == fir or sorted(sec) == sec:
            return True
        return False