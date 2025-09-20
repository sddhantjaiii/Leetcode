from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False
        if len(self.queue) == self.memoryLimit:
            old_source, old_destination, old_timestamp = self.queue.popleft()
            self.packet_set.remove((old_source, old_destination, old_timestamp))
            lst = self.dest_map[old_destination]
            idx = bisect.bisect_left(lst, old_timestamp)
            if idx < len(lst) and lst[idx] == old_timestamp:
                lst.pop(idx)
            if not lst:
                del self.dest_map[old_destination]
        self.queue.append((source, destination, timestamp))
        self.packet_set.add(key)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> list:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packet_set.remove((source, destination, timestamp))
        lst = self.dest_map[destination]
        idx = bisect.bisect_left(lst, timestamp)
        if idx < len(lst) and lst[idx] == timestamp:
            lst.pop(idx)
        if not lst:
            del self.dest_map[destination]
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        lst = self.dest_map[destination]
        left = bisect.bisect_left(lst, startTime)
        right = bisect.bisect_right(lst, endTime)
        return right - left