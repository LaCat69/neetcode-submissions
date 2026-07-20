class TimeMap:

    def __init__(self):
        self.dictonary = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictonary[key].append((timestamp, value))
        print(self.dictonary)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dictonary:
            return ""
        arr = self.dictonary[key]
        l, r = 0, len(arr)-1

        while l <= r:
            m = (l + r) // 2
            guess = arr[m]

            if timestamp == guess[0]:
                return guess[1]
            elif timestamp > guess[0]:
                l = m + 1
            else:
                r = m - 1
        return arr[r][1] if arr[r][0] < timestamp else ""
        
