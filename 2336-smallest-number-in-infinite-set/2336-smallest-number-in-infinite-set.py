from sortedcontainers import SortedList

class SmallestInfiniteSet:

    def __init__(self):
        
        self.smallest = 1
        self.adding = SortedList([math.inf])
        
        
    def popSmallest(self) -> int:
        the_smallest = 0
        if self.smallest < self.adding[0]:
            the_smallest = self.smallest
            self.smallest+=1
        else:
            the_smallest = self.adding.pop(0)
        return the_smallest
            

    def addBack(self, num: int) -> None:
        if self.smallest > num and num not in self.adding:
            self.adding.add(num)