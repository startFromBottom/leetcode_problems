"""

problem link : https://leetcode.com/problems/design-underground-system/
submission detail : https://leetcode.com/contest/weekly-contest-182/submissions/detail/316965599/

"""

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.current = dict()  # key : id, value: (station_name, time)
        self.history = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.current[id]
        del self.current[id]
        start_end = "{} {}".format(start_station, stationName)
        self.history[start_end].append((id, t - start_t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start_end = "{} {}".format(startStation, endStation)
        avg_time = 0
        l = 0
        for each in self.history[start_end]:
            _, t = each
            avg_time += t
            l += 1
        return avg_time / l
