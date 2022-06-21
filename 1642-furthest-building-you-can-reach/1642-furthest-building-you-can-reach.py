class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        cur = heights[0]
        ans = 0
        used_bricks = []
        for i in range(1, len(heights)):
            if cur > heights[i]:
                ans += 1 
            else:
                bisect.insort(used_bricks, heights[i] - cur)
                if heights[i] - cur <= bricks:
                    bricks = bricks - (heights[i] - cur)
                    ans += 1
                else:
                    if ladders > 0:
                        bricks += used_bricks[-1]
                        used_bricks.pop()
                        bricks -= (heights[i] - cur)
                        ladders -= 1
                        ans += 1
                    else:
                        break
            cur = heights[i]
        return ans 
            