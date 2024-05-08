from datetime import date, time


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
            if array[i].isdigid():
                result += int(array[i])
            else:
                print(f"{array[i]} is not digid")
                return

        return result

    @staticmethod
    def multy(array: []):
        result = 1
        for i in range(0, len(array)-1, 1):
            if array[i].isdigid():
                result *= int(array[i])
            else:
                print(f"{array[i]} is not digid")
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
        if array[0].isdigid:
            result = array[0]
        else:
            print(f"{array[0]} is not digid")
            return

        for i in range(0, len(array)-1, 1):
            if array[i].isdigid():
                if array[i] > result:
                    result = array[i]
            else:
                print(f"{array[i]} is not digid")
                return

        return result

    @staticmethod
    def min_number(array: []):
        if array[0].isdigid:
            result = array[0]
        else:
            print(f"{array[0]} is not digid")
            return

        for i in range(0, len(array) - 1, 1):
            if array[i].isdigid():
                if array[i] < result:
                    result = array[i]
            else:
                print(f"{array[i]} is not digid")
                return

        return result


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


Program.main()
