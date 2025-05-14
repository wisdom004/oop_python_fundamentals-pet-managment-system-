#class initialization with default_init_

class Pet:
    def speak(self):
        print("sound made")
        

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())

#a simple class to represent dog with modified _init_
class Dog:
    def __init__(self,name,breed,age = "N/A"):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return f"{self.name} says Woof!"
koba = Dog("Koba","Pitbull",2)
amad = Dog("Amad","Pitbull",)
print(koba.speak())
print(koba.age)
print(amad.age)
    
class Cat:
    pass
class rat:
    pass