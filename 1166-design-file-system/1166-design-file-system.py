class FileSystem:

    def __init__(self):
        self.d = defaultdict()
        

    def createPath(self, path: str, value: int) -> bool:
        if path=="/" or len(path)==0 or path in self.d:
            return False
        parent = path[:path.rfind("/")]
        if len(parent)>1 and parent not in self.d:
            return False
        self.d[path]=value
        return True
    
    def get(self, path: str) -> int:
        return self.d.get(path,-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)