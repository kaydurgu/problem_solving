class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
    
        self.persons = persons
        self.times = times
        self.mp = {}
        temp = defaultdict(int)
        cur_max, now = 0, 0
        for idx, val in enumerate(self.persons):
            temp[val]+=1
            if cur_max <= temp[val]:
                cur_max = temp[val]
                now = val
            self.mp[idx] = now
        
    def q(self, t: int) -> int:
        left = bisect.bisect_left(self.times, t)
        if left<len(self.times):
            if self.times[left] > t:
                left-=1
        else:
            left-=1
        return self.mp[left]
        
        
# person[i] at time times[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)