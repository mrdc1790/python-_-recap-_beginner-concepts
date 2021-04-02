class Dog():
    ## Class object attribute
    ## Same for any instance of this class
    species = 'Mammal'

    def __init__(self, mybreed, name):
        ## user defined Attributes = changed onthe go per object
        ## We take in the argument
        ## Assign it using self.attribute_name
        self.breed = mybreed
        self.name = name
    ## actions/operations --> methods
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")

my_dog = Dog(mybreed='Sheltie',name='Bella')
my_dog.bark(10)