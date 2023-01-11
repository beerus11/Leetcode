from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if (key) not in self.hm:
            return ""
        #print(self.hm)
        values = self.hm[key]
            
        mxT,mxV = values[0]
        for i in range(len(values)-1,-1,-1):
            v = values[i]
            if v[0]<=timestamp:
                return v[1]
        if mxT> timestamp:
            return ""
        return mxV
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)