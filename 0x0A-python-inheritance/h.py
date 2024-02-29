class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

# Creating an instance of the Animal class
generic_animal = Animal(species="Unknown")

class Dog(Animal):
    def __init__(self, breed):
        # Calling the constructor of the superclass (Animal)
        super().__init__(species="Dog")
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        print("Woof!")

# Creating an instance of the Dog class
my_dog = Dog(breed="Labrador")
# Using the Animal instance
print("Generic animal species:", generic_animal.species)
generic_animal.make_sound()  # Output: Generic animal sound

# Using the Dog instance
print("Dog breed:", my_dog.breed)
my_dog.make_sound()  # Output: Woof!

