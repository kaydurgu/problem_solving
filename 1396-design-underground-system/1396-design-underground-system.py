class UndergroundSystem:

    def __init__(self):
        self.mp = defaultdict(list)
        self.betweenStations = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.mp[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        from_station =  self.mp[id][0]
        at_time = self.mp[id][1]
        del self.mp[id]
        
        old_sum, cnt = self.betweenStations.get(f'{from_station}-{stationName}', [0, 0]) 
        old_sum += (t - at_time)
        cnt += 1
        self.betweenStations[f'{from_station}-{stationName}'] = [old_sum, cnt]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.betweenStations[f'{startStation}-{endStation}'][0] / self.betweenStations[f'{startStation}-{endStation}'][1] 


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)