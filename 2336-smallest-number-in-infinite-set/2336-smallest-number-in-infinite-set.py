from sortedcontainers import SortedList

class SmallestInfiniteSet:

    def __init__(self):
        
        self.smallest = 1
        self.adding = SortedList([])
        
    def popSmallest(self) -> int:
        if not self.adding:
            self.smallest+=1
            return self.smallest - 1
        if self.smallest < self.adding[0]:
            self.smallest+=1
            return self.smallest - 1
        return self.adding.pop(0)
    def addBack(self, num: int) -> None:
        if self.smallest > num and num not in self.adding:
            self.adding.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)