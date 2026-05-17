class TimeMap:

    def __init__(self):
        self.dictt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key] = []
        self.dictt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dictt.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            ts, val = values[m]
            if ts <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
        
        return res