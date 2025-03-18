class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyataCar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyataCar("Fortuner")
car2 = ToyataCar("Prius")

print(car1.color)