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