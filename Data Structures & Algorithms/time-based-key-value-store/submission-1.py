from collections import defaultdict
import math

class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: [])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        tuples = self.store[key] if key in self.store else []
        n = len(tuples)

        if not tuples or timestamp < tuples[0][0]:
            return ""

        if timestamp >= tuples[-1][0]:
            return tuples[-1][1]

        # Binary search greatest matching timestamp
        l, r = 0, n-1
        print(f"{timestamp=}, {min(tuples)=}, {max(tuples)=}")

        ts_max = float('-inf')
        v_max = ""
        s = math.ceil(n * math.log2(n)) + 10
        while l <= r and s >= 0:
            s -= 1
            m = l + (r - l)//2
            ts = tuples[m][0]
            print(f"{l=}, {r=}, {ts=}, {timestamp=}")
            if ts <= timestamp:
                if ts >= ts_max:
                    ts_max = ts
                    v_max = tuples[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return v_max

        
