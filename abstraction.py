from abc import ABC,abstractmethod
class Modelcar(ABC):
    @abstractmethod
    def Break1():
        pass
    @abstractmethod
    def speed_up():
        pass
    @abstractmethod
    def speed_down():
        pass
class nexon(Modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop

    def speed_up(self):
        self.speed+=5
        self.stop=False
        print(f'accelerated by 5km/hr and current speed is {self.speed}')

    def Break1(self):
        self.speed+=0
        self.stop=True
    def speed_down(self):
        if not self.stop:
                  self.speed-=5
                  if self.speed==0:
                    self.stop=True
                    print(f'accelerated decreased by 5km/hr and current speed is {self.speed}')

class indica(Modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop

    def speed_up(self):
        self.speed+=2
        self.stop=False
        print(f'accelerated by 2km/hr and current speed is {self.speed}')

    def Break1(self):
        self.speed+=0
        self.stop=True
        
    def speed_down(self):
        if not self.stop:
            self.speed-=2
            if self.speed==0:
                self.stop=True
                print(f'accelerated decreased by 2km/hr and current speed is {self.speed}')




  
