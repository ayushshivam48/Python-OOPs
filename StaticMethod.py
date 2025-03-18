class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    @staticmethod  #decorator function
    def hello():
        print("Hello!!")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name,"your average score is",sum/3)
        
s1 = Student("Ayush Shivam", [99, 98, 97])
s1.hello()
s1.get_avg()