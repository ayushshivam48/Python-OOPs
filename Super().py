class Car:
    
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyataCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        

car1 = ToyataCar("Prius", "Electric")
print(car1.type)