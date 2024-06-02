# region Task 1
class Animal:
    _name: str
    _species: str

    def __init__(self, name: str, species: str):
        self._name = name
        self._species = species

    def make_sound(self):
        print("Sound")


class Dog(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def make_sound(self):
        print("Woof")


class Cat(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def make_sound(self):
        print("Meow")


class Bird(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def make_sound(self):
        print("Chrik")
# endregion


# region Task 2
class Person:
    _name: str
    _age: int
    _profession: str

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._profession = "None"

    def introduce_yourself(self):
        print(f"name: {self._name}, \n"
              f"age: {self._age}")


class Doctor(Person):

    _scalpel_size: float

    def __init__(self, name: str, age: int, scalpel_size: float):
        super().__init__(name, age)
        self._profession = "Doctor"
        self._scalpel_size = scalpel_size

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"scalpel size: {self._scalpel_size}, \n"
              f"profession: {self._profession}\n")


class Engineer(Person):

    __favorite_tool: str

    def __init__(self, name: str, age: int, favorite_tool: str):
        super().__init__(name, age)
        self._profession = "Engineer"
        self.__favorite_tool = favorite_tool

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"favoriteTool: {self.__favorite_tool}, \n"
              f"profession: {self._profession}\n")


class Artist(Person):

    __favorite_color: str

    def __init__(self, name: str, age: int, favorite_color: str):
        super().__init__(name, age)
        self._profession = "Artist"
        self.__favorite_color = favorite_color

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f"favorite_color: {self.__favorite_color}, \n"
              f"profession: {self._profession}\n")
# endregion


# region Task 3
class TransportVehicle:
    pass


class Car(TransportVehicle):
    pass


class Train(TransportVehicle):
    pass


class Express(Train):
    pass
# endregion


# region Task 4
class Animal:
    pass


class Mammal(Animal):
    pass


class Fish(Animal):
    pass


class Cat1(Mammal):
    pass


class Dog1(Mammal):
    pass


class Shark(Fish):
    pass


class Carp(Fish):
    pass
# endregion


class Program:
    @staticmethod
    def main():
        cat = Cat("Mar", "Not")
        cat.make_sound()

        dog = Dog("Bob", "Not")
        dog.make_sound()

        bird = Bird("At", "Not")
        bird.make_sound()

        doc = Doctor("Doc", 53, 12.5)
        engineer = Engineer("Engine", 67, "hammer")
        artist = Artist("Art", 32, "red")

        doc.introduce_yourself()
        engineer.introduce_yourself()
        artist.introduce_yourself()


Program.main()
