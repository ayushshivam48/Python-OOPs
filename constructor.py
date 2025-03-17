class Student:
    
    collage_name = "Amity University"  #class attributr
    
    def __init__(self, name, rollno):   #paramertized constructor
        self.name = name   #obj attributes
        self.rollno = rollno   #obj attributes
        print("adding new student in database....")
        
    def welcome(self):   #methods
        print("Welcome student", self.name)
        
    def get_rollno(self):  #methods
        return self.rollno

print(Student.collage_name)

s1 = Student("Ayush", 4)
s1.welcome()
print("Roll No : ",s1.get_rollno())

s2 = Student("Shivam", 8)
s2.welcome()
print("Roll No : ",s2.get_rollno())