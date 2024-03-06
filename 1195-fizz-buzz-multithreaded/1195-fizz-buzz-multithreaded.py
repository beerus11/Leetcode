class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.ctr = 1
        self.cond = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	with self.cond:    
            while self.ctr <= self.n:    
                if self.ctr % 3 == 0 and self.ctr % 5 != 0:
                    printFizz()
                    self.ctr += 1
                    self.cond.notifyAll()
                else:
                    self.cond.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	with self.cond:    
            while self.ctr <= self.n:
                if self.ctr % 3 != 0 and self.ctr % 5 == 0:
                    printBuzz()
                    self.ctr += 1
                    self.cond.notifyAll()
                else:
                    self.cond.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cond:    
            while self.ctr <= self.n:
                if self.ctr % 3 == 0 and self.ctr % 5 == 0:
                    printFizzBuzz()
                    self.ctr += 1
                    self.cond.notifyAll()
                else:
                    self.cond.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cond:
            while self.ctr <= self.n:
                if self.ctr % 3 != 0 and self.ctr % 5 != 0:
                    printNumber(self.ctr)
                    self.ctr += 1
                    self.cond.notifyAll()
                else:
                    self.cond.wait()