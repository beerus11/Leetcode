from threading import Condition

class H2O:
    def __init__(self):
        self.H = 0
        self.O = 0
        self.cond = Condition()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        with self.cond:
            if self.cond.wait_for(lambda: self.H < 2):
                releaseHydrogen()
                self.H += 1

                if self.H == 2 and self.O == 1:
                    self.H = 0
                    self.O = 0

                self.cond.notify_all()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        with self.cond:
            if self.cond.wait_for(lambda: self.O < 1):
                releaseOxygen()
                self.O += 1

                if self.H == 2 and self.O == 1:
                    self.H = 0
                    self.O = 0

                self.cond.notify_all()