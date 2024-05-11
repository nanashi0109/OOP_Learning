from datetime import date, time
from math import sqrt, pi


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


# Task 3
class ModelWindow:
    def __init__(self, header: str,
                 coordinates_x: int,
                 coordinates_y: int,
                 height: int,
                 width: int,
                 color: str,
                 is_visible: bool,
                 with_frame: bool):
        self.header = header
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y
        self.height = height
        self.width = width
        self.color = color
        self.is_visible = is_visible
        self.with_frame = with_frame

    def moving(self, number_horizontal: int, number_vertical: int, width_screen=1960, height_screen=1080):
        if self.coordinates_x + number_horizontal > width_screen or self.coordinates_x + number_horizontal < 0:
            print("Crosses the border! Try other value")
        else:
            self.coordinates_x += number_horizontal
            print(f"New coordinates x: {self.coordinates_x}")

        if self.coordinates_y + number_vertical > height_screen or self.coordinates_y + number_vertical < 0:
            print("Crosses the border! Try other value")
        else:
            self.coordinates_y += number_vertical
            print(f"New coordinates y: {self.coordinates_y}")

    def change_width(self, number_px, width_screen=1960):
        if self.width + number_px > width_screen or self.width + number_px <= 0:
            print("Incorrect number! Try other number")
        else:
            self.width += number_px
            print(f"New width: {self.width}")

    def change_height(self, number_px, height_screen=1080):
        if self.height + number_px > height_screen or self.height + number_px <= 0:
            print("Incorrect number! Try other number")
        else:
            self.height += number_px
            print(f"New height: {self.height}")

    def change_color(self, new_color: str):
        self.color = new_color
        print(f"New color: {self.color}")

    def change_visibility(self):
        self.is_visible = not self.is_visible
        print(f"Current visibility: {self.is_visible}")

    def change_state_frame(self):
        self.with_frame = not self.with_frame
        print(f"Current with frame: {self.with_frame}")

    def display_status(self):
        print(f"Visibility: {self.is_visible}")
        print(f"With frame: {self.with_frame}")

    def __str__(self):

        return (f"\nHeader: {self.header} \n"
                f"coordinates x: {self.coordinates_x} \n"
                f"coordinates y: {self.coordinates_y} \n"
                f"height: {self.height} \n"
                f"width: {self.width} \n"
                f"color: {self.color} \n"
                f"Is visible: {self.is_visible} \n"
                f"with frame: {self.with_frame}")


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
        if type(other) is int or type(other) is float:
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
        self.denominator = denominator

        self.check_denominator()

    def check_denominator(self):
        if self.denominator == 0:
            print("Denominator equal zero! Please, try other values.")

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


# Task 8
class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        new_hours = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        new_seconds = self.seconds + other.seconds
        new_time = Time(new_hours, new_minutes, new_seconds)
        new_time.time_correction()
        return new_time

    def __sub__(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        new_seconds = self.seconds - other.seconds
        new_time = Time(new_hours, new_minutes, new_seconds)
        new_time.time_correction()
        return new_time

    def __mul__(self, other):
        new_hours = self.hours * other
        new_minutes = self.minutes * other
        new_seconds = self.seconds * other
        new_time = Time(new_hours, new_minutes, new_seconds)
        new_time.time_correction()
        return new_time

    def time_correction(self):
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

        while self.minutes < 0:
            self.hours -= 1
            self.minutes += 60

        while self.seconds < 0:
            self.minutes -= 1
            self.seconds += 60

    def __str__(self):
        if self.hours < 10:
            hours = f"0{self.hours}"
        else:
            hours = self.hours

        if self.minutes < 10:
            minutes = f"0{self.minutes}"
        else:
            minutes = self.minutes

        if self.seconds < 10:
            seconds = f"0{self.seconds}"
        else:
            seconds = self.seconds

        return f"{hours}:{minutes}:{seconds}"


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

        print("\n---Task_3---")
        window_1 = ModelWindow("Window 1", 250, 900, 540, 980, "Red", True, False)

        window_1.change_color("Orange")
        window_1.moving(100, 120)
        window_1.change_state_frame()
        window_1.change_state_frame()
        window_1.change_visibility()
        window_1.display_status()
        print(window_1)

        print("\n---Task_4---")
        array = [1, 5, 2, 76, 17, 251]

        print(f"sum element array: {ArrayUtils.sum(array)}")
        print(f"multy element array: {ArrayUtils.multy(array)}")
        print(f"inversion array: {ArrayUtils.inversion(array)}")
        print(f"max element in array: {ArrayUtils.max_number(array)}")
        print(f"min element in array: {ArrayUtils.min_number(array)}")

        print("\n---Task_5---")
        vec1 = Vector(1, 2, 5)
        vec2 = Vector(2, 3, 7)

        print(f"Sum vectors: {vec1 + vec2}")
        print(f"Sub vectors: {vec1 - vec2}")
        print(f"Multy vectors: {vec1 * vec2}")
        print(f"Scalar multy vector: {vec1 * 3}")
        vec1.length()

        print("\n---Task_6---")
        frac_1 = Fraction(2, 1)
        frac_2 = Fraction(3, 1)

        print(f"Sum fractions: {frac_1 + frac_2}")
        print(f"Sub fractions: {frac_1 - frac_2}")
        print(f"Multy fractions: {frac_1 * frac_2}")

        print("\n---Task_7---")
        print(f"area circle with radius = 5: {GeometryUtils.area_circle(5)}")
        print(f"perimetr circle with radius = 5: {GeometryUtils.perimeter_circle(5)}")
        print(f"area rectangle with width = 5 and height = 10: {GeometryUtils.area_rectangle(5, 10)}")
        print(f"perimetr rectangle with width = 5 and height = 10: {GeometryUtils.perimeter_rectangle(5, 10)}")
        print(f"area triangle with sides (5, 3, 4): {GeometryUtils.area_triangle(5, 3, 4)}")

        print("\n---Task_8---")
        time_1 = Time(3, 45, 30)
        time_2 = Time(4, 30, 45)
        print(time_1 + time_2)
        print(time_2 - time_1)
        print(time_1 * 2)


Program.main()
