#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.avg = defaultdict(dict)
        self.checkin = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin[id]
        del self.checkin[id]
        if start_station in self.avg and stationName in self.avg[start_station]:
            avg, count = self.avg[start_station][stationName]
            self.avg[start_station][stationName] = ((avg*count+(t-start_time))/(count+1), count+1)
        else:
            self.avg[start_station][stationName] = (t-start_time, 1)
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[startStation][endStation][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

