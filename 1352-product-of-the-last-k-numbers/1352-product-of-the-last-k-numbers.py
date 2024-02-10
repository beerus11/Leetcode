class ProductOfNumbers:

    def __init__(self):
        self.prod = []

    def add(self, num: int) -> None:
        if num==0:
            self.prod = []
        elif len(self.prod)==0:
            self.prod.append(num)
        else:
            self.prod.append(self.prod[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if len(self.prod)<k:
            return 0
        if len(self.prod)==k:
            return self.prod[-1]
        return self.prod[-1]//self.prod[len(self.prod)-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)