class Logger:

    def __init__(self):
        self.hm = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hm and timestamp-self.hm[message]<10:
            return False
        self.hm[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)