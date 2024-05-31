from __future__ import annotations


class Library:
    def __init__(self, name: str, address: str, employees: [Employee], books: [Book]) -> None:
        self.__name = name
        self.__address = address
        self.__employees = employees
        self.__books = books

    def get_name(self) -> str:
        return self.__name

    def get_address(self) -> str:
        return self.__address

    def get_employees(self) -> [Employee]:
        return self.__employees

    def get_books(self) -> [Book]:
        return self.__books

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Value must be string.')

        self.__name = name

    def set_address(self, address: str) -> None:
        if not isinstance(address, str):
            raise TypeError('Value must be string.')

        self.__address = address

    def set_employees(self, employees: [Employee]) -> None:
        if not isinstance(employees, list):
            raise TypeError('Value must be Employee.')

        self.__employees = employees

    def set_books(self, books: [Book]) -> None:
        if not isinstance(books, list):
            raise TypeError('Value must be Book.')

        self.__books = books

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError('Value must be Book.')

        if book not in self.__books:
            self.__books.append(book)

    def remove_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError('Value must be Book.')

        if book in self.__books:
            self.__books.remove(book)

    def add_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise TypeError('Value must be Employee.')

        if employee not in self.__employees:
            self.__employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise TypeError('Value must be Employee.')

        if employee in self.__employees:
            self.__employees.remove(employee)

    def __str__(self) -> str:
        return (f"name: {self.__name},\n"
                f"address: {self.__address},\n"
                f"books: {self.__books}\n"
                f"employees: {self.__employees}")


class Book:
    def __init__(self, title: str, author: str, year_realized: int, id: int, genres: [Genre]) -> None:
        self.__title = title
        self.__author = author
        self.__year_realized = year_realized
        self.__id = id
        self.__genres = genres

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_year(self) -> int:
        return self.__year_realized

    def get_id(self) -> int:
        return self.__id

    def get_genres(self) -> list:
        return self.__genres

    def set_title(self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError('Value must be string.')

        self.__title = title

    def set_author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError('Value must be string.')

        self.__author = author

    def set_year(self, year_realized: int) -> None:
        if not isinstance(year_realized, int):
            raise TypeError('Value must be int.')

        self.__year_realized = year_realized

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError('Value must be int.')

        self.__id = id

    def set_genres(self, genres: list) -> None:
        if not isinstance(genres, list):
            raise TypeError('Value must be list.')

        self.__genres = genres

    def add_genre(self, genre: Genre) -> None:
        if not isinstance(genre, list):
            raise TypeError('Value must be list.')

        if genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre) -> None:
        if not isinstance(genre, list):
            raise TypeError('Value must be list.')

        if genre in self.__genres:
            self.__genres.remove(genre)

    def __str__(self) -> str:
        return (f"title: {self.__title},\n"
                f"author: {self.__author},\n"
                f"year: {self.__year_realized},\n"
                f"id: {self.__id},\n"
                f"genres: {self.__genres}")


class Genre:
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Value must be string.')

        self.__name = name

    def set_description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError('Value must be string.')

        self.__description = description

    def __str__(self) -> str:
        return (f"name: {self.__name},\n"
                f"description: {self.__description}")


class Employee:
    def __init__(self, name: str, post: str, id: int, contact_info: [ContactInfo]) -> None:
        self.__name = name
        self.__post = post
        self.__id = id
        self.__contact_info = contact_info

    def get_name(self) -> str:
        return self.__name

    def get_post(self) -> str:
        return self.__post

    def get_id(self) -> int:
        return self.__id

    def get_contact_info(self) -> list:
        return self.__contact_info

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Value must be string.')

        self.__name = name

    def set_post(self, post: str) -> None:
        if not isinstance(post, str):
            raise TypeError('Value must be string.')

        self.__post = post

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError('Value must be int.')

        self.__id = id

    def set_contact_info(self, contact_info: list) -> None:
        if not isinstance(contact_info, list):
            raise TypeError('Value must be list.')

        self.__contact_info = contact_info

    def add_contact_info(self, contact_info: ContactInfo) -> None:
        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Value must be ContactInfo.')

        if contact_info not in self.__contact_info:
            self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info: ContactInfo) -> None:
        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Value must be ContactInfo.')

        if contact_info in self.__contact_info:
            self.__contact_info.remove(contact_info)

    def __str__(self) -> str:
        return (f"name: {self.__name},\n"
                f"post: {self.__post},\n"
                f"id: {self.__id},\n"
                f"contact info: {self.__contact_info}")


class ContactInfo:
    def __init__(self, type_contact: str, value_contact: str) -> None:
        self.__type_contact = type_contact
        self.__value_contact = value_contact

    def get_type(self) -> str:
        return self.__type_contact

    def get_value(self) -> str:
        return self.__value_contact

    def set_type(self, type_contact: str) -> None:
        if not isinstance(type_contact, str):
            raise TypeError('Value must be string.')

        self.__type_contact = type_contact

    def set_value(self, value_contact: str) -> None:
        if not isinstance(value_contact, str):
            raise TypeError('Value must be string.')

        self.__value_contact = value_contact

    def __str__(self) -> str:
        return (f"Type: {self.__type_contact},\n"
                f"Value: {self.__value_contact}")