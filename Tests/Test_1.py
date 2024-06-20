class Animal:
    def __init__(self, name: str, age: int, species: str):
        self._name = name
        self._age = age
        self._species = species

    def show_info(self):
        print(f"{self._name};\t{self._age};\t{self._species}\t", end="")


class Cat (Animal):

    def __init__(self, name, age, species, sex):
        super().__init__(name, age, species)

        self._sex = sex

    def show_info(self):
        print(f"{self._sex}\t", end="")


class Dog(Animal):

    def __init__(self, name, age, species, sex):
        super().__init__(name, age, species)

        self.sex = sex

    def show_info(self):
        print(f"{self.sex}\t", end="")


class CatAndDog(Dog, Cat):
    def __init__(self, name, age, species, sex, color):

        Dog.__init__(self, name, age, species, color)
        Cat.__init__(self, name, age, species, sex)

        self._color = color

    def show_info(self):
        print(f"{self._color}\t", end="")


class SuperCat(Cat):
    def __init__(self,  name, age, species, sex, number_of_kara=0):
        Cat.__init__(self, name, age, species, sex)

        self.__number_of_kara = number_of_kara

    def show_info(self):
        Cat.show_info(self)
        print(f"{self.__number_of_kara}\t", end="")


cat_dog = CatAndDog("Bobik", 15, "NonType", "NonType", "Color")

cat_dog.show_info()
