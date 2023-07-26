class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
    def reset_forward(self):
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head
        

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.reset_forward()
        self.current.next = node
        node.prev = self.current
        self.current = node
        

    def back(self, steps: int) -> str:
        temp = self.current
        while temp.prev and steps>0:
            temp = temp.prev
            steps-=1
        self.current = temp
        return temp.val
            
    def forward(self, steps: int) -> str:
        temp = self.current
        while temp.next and steps>0:
            temp = temp.next
            steps-=1
        self.current = temp
        return temp.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)