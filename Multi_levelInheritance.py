class Car:

    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyataCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(ToyataCar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diseal")
car1.start()