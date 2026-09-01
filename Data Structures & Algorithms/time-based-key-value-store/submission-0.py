class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            current = self.timeMap[key]
            current.append((value, timestamp))
        else:
            self.timeMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        current = self.timeMap[key]
        closest = None
        L, R = 0, len(current) - 1
        while L <= R:
            M = (L + R) // 2
            if current[M][1] == timestamp:
                closest = current[M]
                break
            elif current[M][1] > timestamp:
                R = M - 1
            else:
                L = M + 1
                if not closest or current[M][1] > closest[1]:
                    closest = current[M]
        if closest:
            return closest[0]
        return ""