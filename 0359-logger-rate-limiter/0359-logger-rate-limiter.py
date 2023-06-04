class Logger:

    def __init__(self):
        self.logs = defaultdict(set)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        ans = []
        if timestamp in self.logs and message in self.logs[timestamp]:
            return False
        start = 0 if timestamp-9<0 else timestamp-9
        for i in range(start,timestamp):
            if message == "foo" and timestamp==11:
                print(i,self.logs[i])
            if i in self.logs and message in self.logs[i] :
                return False
        self.logs[timestamp].add(message)
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)