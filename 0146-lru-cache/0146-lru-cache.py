class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        elif len(self)==self.cap:
            self.popitem(last=False)
        self[key]=value
        self.move_to_end(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)