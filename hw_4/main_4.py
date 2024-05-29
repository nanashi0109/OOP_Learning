from __future__ import annotations


# region Task_1
class Student:
    def __init__(self, first_name: str, last_name: str, age: int, average_score: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__average_score = average_score

    # region Getters && Setters
    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_age(self) -> int:
        return self.__age

    def get_average_score(self) -> float:
        return self.__average_score

    def set_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise TypeError('Value must be string.')

        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            raise TypeError('Value must be string.')

        self.__last_name = last_name


    def set_age(self, age: int) -> None:
        if not isinstance(age, str):
            raise TypeError('Value must be int.')

        self.__age = age

    def set_average_score(self, average_score: float) -> None:
        if not isinstance(average_score, str):
            raise TypeError('Value must be float.')

        self.__average_score = average_score

    # endregion

    def __str__(self) -> str:
        return (f"first name: {self.__first_name},\n"
                f"second name: {self.__last_name},\n"
                f"age: {self.__age},\n"
                f"average score: {self.__average_score}")

    def __eq__(self, other: Student) -> bool:
        return True if self.__average_score == other.__average_score else False

    def __ne__(self, other: Student) -> bool:
        return True if self.__average_score != other.__average_score else False

    def __lt__(self, other: Student) -> bool:
        return True if self.__average_score < other.__average_score else False

    def __gt__(self, other: Student) -> bool:
        return True if self.__average_score > other.__average_score else False

    def __le__(self, other: Student) -> bool:
        return True if self.__average_score <= other.__average_score else False

    def __ge__(self, other: Student) -> bool:
        return True if self.__average_score >= other.__average_score else False

# endregion


class Program:
    @staticmethod
    def main():
        first_student = Student("AAA", "aaa", 15, 512.2)
        second_student = Student("BBB", "bbb", 45, 512.2)

        print(first_student == second_student)
        print(first_student != second_student)
        print(first_student > second_student)
        print(first_student < second_student)
        print(first_student >= second_student)
        print(first_student <= second_student)


Program.main()
