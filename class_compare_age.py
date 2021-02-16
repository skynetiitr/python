class person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            print("Same Age")
        else:
            print("Different Age")


c1 = person('Anshul', 27)

c2 = person('Bharat', 29)

print(c1.name, c1.age)
print(c2.name, c2.age)

c1.compare(c2)

