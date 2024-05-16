class Library:

    count_register_user = 0

    def __init__(self, name: str, address: str, book_list: list, user_list: list):
        self.name = name
        self.address = address
        self.book_list = book_list
        self.user_list = user_list

    def add_book(self, book: "Book"):
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")

        if self.book_list.count(book) == 0:
            self.book_list.append(book)
            book.set_stock(True)
            print(f"In library add book {book.name}")

    def remove_book(self, book: "Book"):
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")

        if self.book_list.count(book) > 0:
            self.book_list.remove(book)
            book.set_stock(False)
            print(f"In library remove book {book.name}")

    def register_user(self, user: "User"):
        if not isinstance(user, User):
            raise TypeError("User must be User")

        if self.user_list.count(user) == 0:
            self.user_list.append(user)
            self.count_register_user += 1
            user.set_number_library_card(self.count_register_user)
            print(f"Register user {user.name} by number {self.count_register_user}")

    def issue_book(self, book: "Book", user: "User"):
        if not isinstance(book, Book) or not isinstance(user, User):
            raise TypeError("User must be User/Book must be Book")

        if self.book_list.count(book) == 0 or (not book.is_stock):
            print(f"Book {book.name} is not in library")
            return

        book.set_stock(False)
        book.set_user(user)
        user.take_book(book)
        print(f"User {user.name} take book {book.name}")

    def return_book(self, book: "Book", user: "User"):
        if not isinstance(book, Book) or not isinstance(user, User):
            raise TypeError("User must be User/Book must be Book")

        if self.book_list.count(book) == 0:
            self.add_book(book)

        book.set_stock(True)
        book.set_user(None)
        user.remove_book(book)
        print(f"User {user.name} returned book {book.name}")

    def get_book_status(self) -> str:
        result = "Book status: \n"
        for book in self.book_list:
            result += f"{book} \n"

        return result

    def get_user_status(self) -> str:
        result = "User status: \n"
        for user in self.user_list:
            result += f"{user} \n"

        return result

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}, Book List: {self.book_list}, User list: {self.user_list}\n"


class Book:
    def __init__(self, name: str, author: str, year_release: int, genre: str, is_stock: bool, current_user):
        self.name = name
        self.author = author
        self.year_release = year_release
        self.genre = genre
        self.is_stock = is_stock
        self.current_user = current_user

    def set_stock(self, is_stock: bool):
        if not isinstance(is_stock, bool):
            raise TypeError("is_stock must be bool")

        self.is_stock = is_stock

    def set_user(self, user: "User"):
        if isinstance(user, User) or isinstance(user, type(None)):
            self.current_user = user

    def set_genre(self, new_genre: str):
        if not isinstance(new_genre, str):
            raise TypeError("new_genre must be str")

        self.genre = new_genre

    def is_stock_in_library(self):
        return self.is_stock

    def __str__(self):
        result = (f"Name: {self.name}, author: {self.author}, "
                f"year_release: {self.year_release}, genre: {self.genre}, "
                f"current_user: ")

        if isinstance(self.current_user, User):
            result += f"{self.current_user.name}"
        else:
            result += f"{self.current_user}"

        return result


class User:
    def __init__(self, name: str, number_library_card: int, taken_books: list):
        self.name = name
        self.number_library_card = number_library_card
        self.taken_books = taken_books

    def take_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")

        self.taken_books.append(book)

    def remove_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")

        if self.taken_books.count(book) > 0:
            self.taken_books.remove(book)

    def get_taken_books(self):
        return self.taken_books

    def set_number_library_card(self, new_number_library_card: int):
        if not isinstance(new_number_library_card, int):
            raise TypeError("new_number_library_card must be int")

        self.number_library_card = new_number_library_card

    def __str__(self):
        result = f"name: {self.name}, number_library_card: {self.number_library_card}, books: "
        for book in self.taken_books:
            result += f"{book.name} "

        return result


class Program:
    @staticmethod
    def main():
        user_1 = User("Stas", 1231, [])
        library_1 = Library("Kray", "SSSSSSssSSS", [], [])
        book_1 = Book("King Arthur", "NAAANI", 0, "Action", False, None)
        book_2 = Book("Clear code", "Robert Martin", 2022, "educational", False, None)

        library_1.register_user(user_1)
        library_1.add_book(book_1)
        library_1.add_book(book_2)

        library_1.issue_book(book_1, user_1)
        library_1.issue_book(book_2, user_1)
        print(library_1.get_book_status())
        print(library_1.get_user_status())
        library_1.return_book(book_1, user_1)
        print(library_1.get_book_status())


Program.main()
