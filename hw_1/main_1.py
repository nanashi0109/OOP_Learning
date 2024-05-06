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
    def __init__(self, maker: str, model: str, passenger_capacity: int, current_height: int, current_velocity: int):
        self.maker = maker
        self.model = model
        self.passenger_capacity = passenger_capacity
        self.current_height = current_height
        self.current_velocity = current_velocity

    def take_off_plane(self):
        print("Take off plane")

    def landing_plane(self):
        print("Landing plane")

    def change_height(self, new_height: int):
        if new_height < 0:
            print("ERROR! You can`t be so low")
        else:
            self.current_height = new_height

    def change_velocity(self, new_velocity: int):
        if new_velocity < 0:
            print("ERROR! You can`t have negative velocity")
        else:
            self.current_velocity = new_velocity

    def print_data(self):
        print(f"Maker: {self.maker}")
        print(f"Model: {self.model}")
        print(f"Max count passenger: {self.passenger_capacity}")
        print(f"Current height: {self.current_height}")
        print(f"Current velocity: {self.current_velocity}")