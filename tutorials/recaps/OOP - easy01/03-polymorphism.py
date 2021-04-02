class Animal():
    def __init__ (self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+" says WOOF!"

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name+" says MEOW!"

niko = Dog("Niko")
felix = Cat("Felix")

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

fido = Dog("Fido")
sparkle = Cat("Sparkle")
print(fido.speak())
print(sparkle.speak())

