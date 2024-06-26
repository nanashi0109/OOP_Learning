# Task 1
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


# Task 2
class Book:
    def __init__(self, name: str, author: str, count_page: int):
        self.name = name
        self.author = author
        self.count_page = count_page

    def open_page(self, page: int):
        if page > self.count_page:
            print("ERROR! Count page is so large!")
        elif page < 0:
            print("ERROR! Page is so small!")
        else:
            print(f"Opening page: {page}")

    def print_data(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Count page: {self.count_page}")


# Task 3
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


# Task 4
class MusicAlbum:
    def __init__(self, artist: str, album_name: str, genre: str, track_list: []):
        self.artist = artist
        self.album_name = album_name
        self.genre = genre
        self.track_list = track_list

    def add_songs_in_album(self, tracks_names: str):
        self.track_list.append(tracks_names)
        print(f"In album adding: {tracks_names}")

    def remove_song_in_album(self, tracks_names: str):
        self.track_list.remove(tracks_names)
        print(f"In album remove: {tracks_names}")

    def play_song_in_album(self, track_name: str):
        if self.track_list.count(track_name) > 0:
            print(f"Play {track_name}")
        else:
            print(f"ERROR! Track {track_name} doesn't find!")

    def print_data(self):
        print(f"Artist: {self.artist}")
        print(f"Album: {self.album_name}")
        print(f"Genre: {self.genre}")
        print(f"Track list: {self.track_list}")


class Program:
    @staticmethod
    def main():
        print("---Task_1---")
        a1 = Animal("Cat Boris", 2, "MEOW MEOW")
        a1.play_sound()
        a1.print_data()

        print("\n ---Task_2---")
        book1 = Book("Crime and punishment", "Dostoevsky", 672)
        book1.open_page(1232)
        book1.open_page(523)
        book1.print_data()

        print("\n ---Task_3---")
        passenger_plane1 = PassengerPlane("some famous builder", "ARC100 FC72", 222, 100, 300)
        passenger_plane1.take_off_plane()
        passenger_plane1.change_height(-100)
        passenger_plane1.change_height(2500)
        passenger_plane1.change_velocity(500)
        passenger_plane1.landing_plane()
        passenger_plane1.print_data()

        print("\n ---Task_4---")
        album1 = MusicAlbum("NEWLIGHTCHILD", "NIGHT FOR EVER", "electro rok", [])

        album1.add_songs_in_album("GESHTALT")
        album1.add_songs_in_album("AMORE")
        album1.add_songs_in_album("VIP")

        album1.remove_song_in_album("AMORE")
        album1.play_song_in_album("AMORE")
        album1.play_song_in_album("VIP")
        album1.print_data()


Program.main()
