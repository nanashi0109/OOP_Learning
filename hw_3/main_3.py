# Task 1.2

class Spell:
    def __init__(self, name: str, difficulty_level: float,
                 type: str, description: str) -> None:
        self.__name = name
        self.__difficulty_level = difficulty_level
        self.__type = type
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_difficulty_level(self) -> float:
        return self.__difficulty_level

    def get_type(self) -> str:
        return self.__type

    def get_description(self) -> str:
        return self.__description

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Value must be type str")

        self.__name = name

    def set_difficulty_level(self, difficulty_level: float) -> None:
        if not isinstance(difficulty_level, float):
            raise TypeError("Value must be type float")

        self.__difficulty_level = difficulty_level

    def set_type(self, type: str) -> None:
        if not isinstance(type, str):
            raise TypeError("Value must be type str")

        self.__type = type

    def set_description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Value must be type str")

        self.__description = description

    def __str__(self) -> str:
        return (f"name: {self.__name}\n"
                f"difficulty_level: {self.__difficulty_level}\n"
                f"type: {self.__type}\n"
                f"description: {self.__description}")


# Task 1.1
class Wizard:
    def __init__(self, name: str, faculty: str,
                 level_magical_power: float,
                 known_spells: [Spell],
                 is_released: bool):
        self.__name = name
        self.__faculty = faculty
        self.__level_magical_power = level_magical_power
        self.__known_spells = known_spells
        self.__is_released = is_released

    def get_name(self) -> str:
        return self.__name

    def get_faculty(self) -> str:
        return self.__faculty

    def get_level_magical_power(self) -> float:
        return self.__level_magical_power

    def get_spells(self) -> [Spell]:
        return self.__known_spells

    def is_released(self) -> bool:
        return self.__is_released

    def set_faculty(self, faculty: str) -> None:
        if not isinstance(faculty, str):
            raise TypeError("value must be string")

        self.__faculty = faculty

    def set_magic_level(self, level_magical_power: float) -> None:
        if not isinstance(level_magical_power, float):
            raise TypeError("value must be type float ")

        self.__level_magical_power = level_magical_power

    def set_released(self, is_released: bool) -> None:
        if not isinstance(is_released, bool):
            raise TypeError("value must be type bool")
        self.__is_released = is_released

    def add_spell(self, spell: Spell) -> None:
        if not isinstance(spell, Spell):
            raise TypeError("value must be type Spell")
        if spell not in self.__known_spells:
            self.__known_spells.append(spell)

    def remove_spell(self, spell: Spell) -> None:
        if not isinstance(spell, Spell):
            raise TypeError("value must be type Spell")

        if spell in self.__known_spells:
            self.__known_spells.remove(spell)

    def increase_magical_level(self, amount: float) -> None:
        if not isinstance(amount, float):
            raise TypeError("value must be type float")

        self.__level_magical_power += amount

    def decrease_magical_level(self, amount: float) -> None:
        if not isinstance(amount, float):
            raise TypeError("value must be type float")

        self.__level_magical_power -= amount

    def __str__(self) -> str:
        result = ""
        for spell in self.__known_spells:
            result += str(spell) + ", \n"

        return (f"name: {self.__name} \n"
                f"faculty: {self.__faculty}\n"
                f"level: {self.__level_magical_power}\n"
                f"is_released: {self.__is_released}\n"
                f"Spells: {result}")


# Task 2
class Project:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return self.__name


class Employee:
    def __init__(self, name: str, post: str, department: str, salary: float,
                 work_experience: int, completed_projects: [Project]) -> None:
        self.__name = name
        self.__post = post
        self.__department = department
        self.__salary = salary
        self.__work_experience = work_experience
        self.__completed_projects = completed_projects

    def get_name(self) -> str:
        return self.__name

    def get_post(self) -> str:
        return self.__post

    def get_department(self) -> str:
        return self.__department

    def get_salary(self) -> float:
        return self.__salary

    def get_work_experience(self) -> float:
        return self.__work_experience

    def get_completed_projects(self) -> [Project]:
        return self.__completed_projects

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Value must be type str")

        self.__name = name

    def set_post(self, post: str) -> None:
        if not isinstance(post, str):
            raise TypeError("Value must be type str")

        self.__post = post

    def set_department(self, department: str) -> None:
        if not isinstance(department, str):
            raise TypeError("Value must be type str")

        self.__department = department

    def set_salary(self, salary: float) -> None:
        if not isinstance(salary, float):
            raise TypeError("Value must be type float")

        self.__salary = salary

    def set_work_experience(self, work_experience: int) -> None:
        if not isinstance(work_experience, int):
            raise TypeError("Value must be type int")

        self.__work_experience = work_experience

    def set_completed_projects(self, completed_projects: [Project]) -> None:
        self.__completed_projects = completed_projects

    def add_completed_project(self, project: Project) -> None:
        if not isinstance(project, Project):
            raise TypeError("value must be type Project")

        if project not in self.__completed_projects:
            self.__completed_projects.append(project)

    def remove_completed_project(self, project: Project) -> None:
        if not isinstance(project, Project):
            raise TypeError("value must be type Project")

        if project in self.__completed_projects:
            self.__completed_projects.remove(project)

    def increase_salary(self, amount: float) -> None:
        if not isinstance(amount, float):
            raise TypeError("value must be type float")

        self.__salary += amount

    def __str__(self) -> str:
        result = ""
        for project in self.__completed_projects:
            result += str(project) + ", "

        return (f"name: {self.__name} \n"
                f"post: {self.__post} \n"
                f"department: {self.__department} \n"
                f"salary: {self.__salary} \n"
                f"work_experience: {self.__work_experience} \n"
                f"completed_projects: {result}")


# Task 3
class Robot:
    def __init__(self, serial_number: str, model: str,
                 current_task, battery: float, is_working) -> None:
        self.__serial_number = serial_number
        self.__model = model
        self.__current_task = current_task
        self.__battery = battery
        self.__is_working = is_working

    def turn_on(self):
        self.__is_working = True

    def turn_off(self):
        self.__is_working = False

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_model(self) -> str:
        return self.__model

    def get_current_task(self) -> str:
        return self.__current_task

    def get_battery(self) -> float:
        return self.__battery

    def is_working(self) -> bool:
        return self.__is_working

    def set_serial_number(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("value must be type str")

        self.__serial_number = name

    def set_model(self, model: str) -> None:
        if not isinstance(model, str):
            raise TypeError("value must be type str")

        self.__model = model

    def set_task(self, task: str) -> None:
        if not isinstance(task, str):
            raise TypeError("value must be type str")

        self.__current_task = task

    def set_battery(self, battery: float) -> None:
        if not isinstance(battery, float):
            raise TypeError("value must be type float")

        self.__battery = battery

    def set_working(self, is_working: bool) -> None:
        if not isinstance(is_working, bool):
            raise TypeError("value must be type bool")

        self.__is_working = is_working

    def __str__(self) -> str:
        return (f"serial_number: {self.__serial_number} \n"
                f"model: {self.__model} \n"
                f"current_task: {self.__current_task} \n"
                f"battery: {self.__battery} \n"
                f"is working: {self.__is_working}")


# Task 4
class Achievement:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self):
        return self.__name


class Athlete:
    def __init__(self, name: str, age: int, sport_type: str,
                 achievements: [Achievement], is_functional: bool) -> None:
        self.__name = name
        self.__age = age
        self.__sport_type = sport_type
        self.__achievements = achievements
        self.__is_functional = is_functional

    def add_achievement(self, achievement: Achievement) -> None:
        if not isinstance(achievement, Achievement):
            raise TypeError("value must be type Achievement")

        if achievement not in self.__achievements:
            self.__achievements.append(achievement)

    def remove_achievement(self, achievement: Achievement) -> None:
        if not isinstance(achievement, Achievement):
            raise TypeError("value must be type Achievement")

        if achievement in self.__achievements:
            self.__achievements.remove(achievement)

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_sport_type(self) -> str:
        return self.__sport_type

    def get_achievements(self) -> [Achievement]:
        return self.__achievements

    def is_functional(self) -> bool:
        return self.__is_functional

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("value must be type str")

        self.__name = name

    def set_age(self, age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("value must be type int")

        self.__age = age

    def set_sport_type(self, sport_type: str) -> None:
        if not isinstance(sport_type, str):
            raise TypeError("value must be type str")

        self.__sport_type = sport_type

    def set_achievements(self, achievements: [Achievement]) -> None:
        self.__achievements = achievements

    def set_is_functional(self, is_functional: bool) -> None:
        if not isinstance(is_functional, bool):
            raise TypeError("value must be type bool")

        self.__is_functional = is_functional

    def __str__(self) -> str:
        result = ""
        for achievement in self.__achievements:
            result += str(achievement) + ", "

        return (f"name: {self.__name} \n"
                f"age: {self.__age} \n"
                f"sport_type: {self.__sport_type} \n"
                f"achievements: {result} \n"
                f"is functional: {self.__is_functional}")


class Program:
    @staticmethod
    def main():
        print("---Task_1---")
        spell_1 = Spell("first", 12, "Attack", "Some description")
        spell_2 = Spell("second", 25, "Heal", "More description")

        wizard_1 = Wizard("first", "Slytherin", 234, [spell_1], False)

        wizard_1.add_spell(spell_2)
        wizard_1.add_spell(spell_1)

        wizard_1.is_released()
        print(wizard_1)
        print(spell_1)

        print("\n---Task_2---")
        project_1 = Project("first project")
        project_2 = Project("second project")

        emp_1 = Employee("first", "Manager", "main", 50500, 5, [project_1, project_2])
        emp_1.add_completed_project(project_2)
        print(emp_1)

        print("\n---Task_3---")
        robot_1 = Robot("02515FaT", "Killer", "Clear office", 48, True)
        robot_1.set_task("Kill boss")
        print(robot_1)

        print("\n---Task_4---")
        athlete = Athlete("Athlete name", 53, "Powerlifting", [Achievement("some achievement")], True)
        athlete.add_achievement(Achievement("second achievement"))
        print(athlete)


Program.main()
