#Task 1
class Animal:
    def __init__(self, name: str, age: int, sound: str):
        self.name = name
        self.age = age
        self.sound = sound

    def play_sound(self):
        print(f"Animal scream: {self.sound}")

    def print_data(self):
        print(f"Animal's name: {self.name}")
        print(f"Animal's age: {self.age}")
        print(f"Animal's sound: {self.sound}")


#Task 2
class Book:
    def __init__(self, name: str, author: str, count_page: int):
        self.name = name
        self.author = author
        self.count_page = count_page

    def open_page(self, page: int):
        if page > self.count_page:
            print("ERROR! Count page is so large!")
        elif page <0:
            print("ERROR! Page is so small!")
        else:
            print(f"Opening page: {page}")

    def print_date(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Count page: {self.count_page}")

class PassengerPlane:
    def __init__(self):
        pass

    def take_off_plane(self):
        pass
    def landing_plane(self):
        pass
    def change_height(self):
        pass
    def change_velocity(self):
        pass
    def print_data(self):
        pass