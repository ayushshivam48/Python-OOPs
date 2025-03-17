class Person:
    name = "Anonoymous"
    
    @classmethod
    def changename(cls, name):
        cls.name = name
        
p1 = Person()
p1.changename("Ayush Shivam")
print(p1.name)
print(Person.name)