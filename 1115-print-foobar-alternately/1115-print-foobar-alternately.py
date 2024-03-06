class FooBar:
    def __init__(self, n):
        self.n = n
        self.count =0
        self.cond = threading.Condition()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cond:
                while self.count%2!=0:
                    self.cond.wait()
            
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.count+=1
                self.cond.notify()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cond:
                while self.count%2==0:
                    self.cond.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.count+=1
                self.cond.notify()
                
                