class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        boxTypes.reverse()
        ans = 0
        for x, y in boxTypes:
            if truckSize-x>=0:
                ans+=(x * y)
                truckSize-=x
            else:
                ans+=(truckSize*y) 
                truckSize = 0
        return ans