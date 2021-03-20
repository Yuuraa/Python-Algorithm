from collections import defaultdict
class UndergroundSystem:
    from collections import defaultdict
    def __init__(self):
        self.check_ins = {}
        self.times = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, startStation = self.check_ins[id]
        del(self.check_ins[id])
        self.times[startStation + stationName].append(t - start_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[startStation + endStation])/ len(self.times[startStation + endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)