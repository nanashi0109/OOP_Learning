from datetime import date, time
from math import sqrt
from math import pi


# Task 1
class Patient:
    def __init__(self, first_name: str, second_name: str, last_name: str, age: int, current_illness: str):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age
        self.current_illness = current_illness

    def make_appointment(self, date_app: date, time_app: time):
        print(f"You, {self.first_name} {self.last_name},  signed up for date: {date_app}, time: {time_app}")

    def __str__(self):
        return f"{self.first_name} \n{self.second_name} \n{self.last_name} \n{self.age} \n{str(self.current_illness)}"


# Task 2
class TouristSpot:
    def __init__(self, name_place: str, country: str, type_landmark: str):
        self.name_place = name_place
        self.country = country
        self.type = type_landmark

    def visit_landmark(self, name_visitor):
        print(f"{name_visitor} visited the {self.name_place}")

    def __str__(self):
        return f"{self.name_place} \n{self.country} \n{self.type}"


# Task 4
class ArrayUtils:
    @staticmethod
    def sum(array: []):
        result = 0
        for i in range(0, len(array)-1, 1):
            if str(array[i]).isdigit():
                result += int(array[i])
            else:
                print(f"{array[i]} is not convertable")
                return

        return result

    @staticmethod
    def multy(array: []):
        result = 1
        for i in range(0, len(array)-1, 1):
            if str(array[i]).isdigit():
                result *= int(array[i])
            else:
                print(f"{array[i]} is not convertable")
                return

        return result

    @staticmethod
    def inversion(array: []):
        result = []
        for i in range(len(array)-1, 0, -1):
            result.append(array[i])

        return result

    @staticmethod
    def max_number(array: []):
        if str(array[0]).isdigit():
            result = array[0]
        else:
            print(f"{array[0]} is not convertable")
            return

        for i in range(0, len(array)-1, 1):
            if str(array[i]).isdigit():
                if array[i] > result:
                    result = array[i]
            else:
                print(f"{array[i]} is not convertable")
                return

        return result

    @staticmethod
    def min_number(array: []):
        if str(array[0]).isdigit():
            result = array[0]
        else:
            print(f"{array[0]} is not convertable")
            return

        for i in range(0, len(array) - 1, 1):
            if str(array[i]).isdigit():
                if array[i] < result:
                    result = array[i]
            else:
                print(f"{array[i]} is not convertable")
                return

        return result


# Task 5
class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z

        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        if type(other) is int:
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other

            return Vector(new_x, new_y, new_z)

        elif type(other) is Vector:
            new_x = self.y * other.z - self.z * other.y
            new_y = -(self.x * other.z - self.z * other.x)
            new_z = self.x * other.y - self.y * other.x

            return Vector(new_x, new_y, new_z)

    def length(self):
        length_vector = sqrt(self.x**2 + self.y**2 + self.z**2)
        return length_vector

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


# Task 6
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator

    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_denominator = self.numerator * other.denominator
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator

        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.numerator

        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return "0"
        else:
            return f"{self.numerator}/{self.denominator}"


# Task 7
class GeometryUtils:
    @staticmethod
    def area_circle(radius: float):
        return pi * radius ** 2

    @staticmethod
    def perimeter_circle(radius: float):
        return 2 * pi * radius

    @staticmethod
    def area_rectangle(width: float, height: float):
        return width * height

    @staticmethod
    def perimeter_rectangle(width: float, height: float):
        return 2 * (width + height)

    @staticmethod
    def area_triangle(first_side: float, second_side: float, third_side: float):
        p = (first_side + second_side + third_side) / 2
        return sqrt(p*(p-first_side)*(p-second_side)*(p-third_side))


class Program:
    @staticmethod
    def main():
        print("\n---Task_1---")
        patient = Patient("San", "Girkin", "Sanych", 52, "pneumonia")

        patient.make_appointment(date(2020, 1, 1), time(9, 30))
        print(patient)

        print("\n---Task_2---")
        tourist_spot = TouristSpot("State of Liberty", "New York", "historical")

        tourist_spot.visit_landmark(patient.first_name + " " + patient.last_name)
        print(tourist_spot)

        print("\n---Task_4---")
        array = [1, 5, 2, 76, 17, 251]

        print(ArrayUtils.sum(array))
        print(ArrayUtils.multy(array))
        print(ArrayUtils.inversion(array))
        print(ArrayUtils.max_number(array))
        print(ArrayUtils.min_number(array))

        print("\n---Task_5---")
        vec1 = Vector(1, 2, 5)
        vec2 = Vector(2, 3, 7)

        print(vec1 + vec2)
        print(vec1 - vec2)
        print(vec1 * vec2)
        print(vec1 * 3)
        vec1.length()

        print("\n---Task_6---")
        frac_1 = Fraction(2, 1)
        frac_2 = Fraction(3, 1)

        print(frac_1 + frac_2)
        print(frac_1 - frac_2)
        print(frac_1 * frac_2)

        print("\n---Task_7---")
        print(GeometryUtils.area_circle(5))
        print(GeometryUtils.perimeter_circle(5))
        print(GeometryUtils.area_rectangle(5, 10))
        print(GeometryUtils.perimeter_rectangle(5, 10))
        print(GeometryUtils.area_triangle(5, 3, 4))


Program.main()
