from __future__ import annotations
import random


class HogwartsStudent:
    def __init__(self, name: str, hogwarts_house: str, mana: float = 100.0, learned_spells: [Spell] = None):
        self.__name = name
        self.__hogwarts_house = hogwarts_house
        self.__mana = mana
        self.__learned_spells = learned_spells

        self.__min_cost_spell = 0
        self.__calculate_min_cost_spell()

    # region Getters && Setters
    def get_name(self) -> str:
        return self.__name

    def get_hogwarts_house(self) -> str:
        return self.__hogwarts_house

    def get_mana(self) -> float:
        return self.__mana

    def get_learned_spells(self) -> [Spell]:
        return self.__learned_spells

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Value must be string")

        self.__name = name

    def set_hogwarts_house(self, hogwarts_house: str) -> None:
        if not isinstance(hogwarts_house, str):
            raise TypeError("Value must be str")

        self.__hogwarts_house = hogwarts_house

    def set_mana(self, mana: float) -> None:
        if not isinstance(mana, float):
            raise TypeError("Value must be float")

        self.__mana = mana

    def set_learned_spells(self, learned_spells: [Spell]) -> None:
        if not isinstance(learned_spells, list):
            raise TypeError("Value must be list")

        self.__learned_spells = learned_spells
        self.__calculate_min_cost_spell()
    # endregion

    def __calculate_min_cost_spell(self) -> None:
        self.__min_cost_spell = self.__learned_spells[0].get_mana_cost()

        for spell in self.__learned_spells:
            if spell.get_mana_cost() < self.__min_cost_spell:
                self.__min_cost_spell = spell.get_mana_cost()
        print(f"Min cost spell: {self.__min_cost_spell}")

    def learn_spell(self, spell: Spell) -> None:
        if not isinstance(spell, Spell):
            raise TypeError("Value must be Spell")

        if spell not in self.__learned_spells:
            self.__learned_spells.append(spell)
            self.__calculate_min_cost_spell()

    def can_attacking(self) -> bool:
        return self.__mana >= self.__min_cost_spell

    def cast_spell(self, target: HogwartsStudent) -> None:
        # spell_index = random.randint(0, len(self.__learned_spells) - 1)
        # spell_for_attack = self.__learned_spells[spell_index]
        spell_for_attack = random.choice(self.__learned_spells)

        if self.__mana - spell_for_attack.get_mana_cost() >= 0:
            self.__mana -= spell_for_attack.get_mana_cost()
            spell_for_attack.cast(target)
            print(f"{self.__name} mana: {self.__mana}")
        else:
            print(f"{self.__name} skip a turn")

    def __str__(self) -> str:
        return (f"Name {self.__name}, Hogwarts: {self.__hogwarts_house}, "
                f"mana: {self.__mana}, learned_spells: {self.__learned_spells}")


class Spell:
    def __init__(self, name: str, description: str, mana_cost: float):
        self.__name = name
        self.__description = description
        self.__mana_cost = mana_cost

    # region Getters && Setters
    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_mana_cost(self) -> float:
        return self.__mana_cost

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Value must be string")

        self.__name = name

    def set_description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Value must be string")

        self.__description = description

    def set_mana_cost(self, mana_cost: float) -> None:
        if not isinstance(mana_cost, float):
            raise TypeError("Value must be float")

        self.__mana_cost = mana_cost
    # endregion

    def cast(self, target: HogwartsStudent) -> None:
        print(f"The {target.get_name()} was attacked by a {self.__name}.")

    def __str__(self):
        return (f"name: {self.__name}, description: {self.__description}, "
                f"mana_cost: {self.__mana_cost}.")


class Hogwarts:
    def __init__(self, students: [HogwartsStudent] = None, spells: [Spell] = None):
        self.__students = students
        self.__spells = spells

    # region Getters && Setters
    def get_students(self) -> [HogwartsStudent]:
        return self.__students

    def get_spells(self) -> [Spell]:
        return self.__spells

    def set_students(self, students: [HogwartsStudent]) -> None:
        if not isinstance(students, list):
            raise TypeError("Value must be list")

        self.__students = students

    def set_spells(self, spells: [Spell]) -> None:
        if not isinstance(spells, list):
            raise TypeError("Value must be list")

        self.__spells = spells
    # endregion

    def enroll_student(self, student: HogwartsStudent) -> None:
        if not isinstance(student, HogwartsStudent):
            raise TypeError("Value must be HogwartsStudent")

        if student not in self.__students:
            self.__students.append(student)

    def tech_spell(self, spell: Spell) -> None:
        if not isinstance(spell, Spell):
            raise TypeError("Value must be Spell")

        if spell not in self.__spells:
            self.__spells.append(spell)

    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent) -> None:
        while student1.can_attacking() and student2.can_attacking():
            student1.cast_spell(student2)
            student2.cast_spell(student1)
            print("------")

        if not student1.can_attacking():
            print(f"The student({student1.get_name()}) has not enough mana!")
        else:
            print(f"The student({student2.get_name()}) has enough mana!")


class Program:
    @staticmethod
    def main():
        expelliarmus = Spell("Expelliarmus", "Дизармирование противника", 15.0)
        stupefy = Spell("Stupefy", "Оглушение противника", 45.0)
        avada_kedavra = Spell("Avada Kedavra", "Смертельное ранение", 95.0)
        protego = Spell("Protego", "Защитный щит, отражающий заклинания", 20.0)
        petrificus_totalus = Spell("Petrificus Totalus", "Полная парализация противника", 40.0)
        lumos = Spell("Lumos", "Создание источника света на конце волшебной палочки", 5.0)
        expecto_patronum = Spell("Expecto Patronum", "Призывание патронуса для защиты от дементоров", 80.0)


        stud1 = HogwartsStudent("First", "first_house", 123.3,
                                [expecto_patronum, lumos, expelliarmus, protego])

        stud2 = HogwartsStudent("Second", "second_house", 534.2,
                                [avada_kedavra, petrificus_totalus, stupefy, protego])

        hogwarts = Hogwarts([stud1, stud2], [expelliarmus, stupefy, avada_kedavra, protego])
        hogwarts.tech_spell(petrificus_totalus)
        hogwarts.tech_spell(lumos)
        hogwarts.tech_spell(expecto_patronum)

        hogwarts.simulate_duel(stud1, stud2)


Program.main()
