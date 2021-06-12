class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"My name is {self.name} , I am {self.age} years old ."
    def sound(self):
        return f"mewww"

cat1=cat("Pussy",3)
cat2=cat("doggy",4)

print(cat.details(cat2))
print(cat.details(cat1))
print(cat.sound(cat1))
