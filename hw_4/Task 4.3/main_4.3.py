class Car:
    def __init__(self, brand: str, model: str, year_release: int, price: float, status: str = "expected"):
        self.__brand = brand
        self.__model = model
        self.__year_release = year_release
        self.__price = price
        self.__status = status

    def get_brand(self) -> str:
        return self.__brand

    def get_model(self) -> str:
        return self.__model

    def get_year_release(self) -> int:
        return self.__year_release

    def get_price(self) -> float:
        return self.__price

    def get_status(self) -> str:
        return self.__status

    def set_price(self, price: float) -> None:
        if not isinstance(price, float):
            raise TypeError("Value must be float")

        self.__price = price

    def set_status(self, status: str) -> None:
        if not isinstance(status, str):
            raise TypeError("Value must be str")

        self.__status = status

    def __str__(self):
        return f"brand: {self.__brand}, model: {self.__model}"


class Salesperson:
    def __init__(self, name: str, work_experience: int, cars_sold: [Car] = None):
        self.__name = name
        self.__work_experience = work_experience
        self.__cars_sold = cars_sold

    def get_name(self) -> str:
        return self.__name

    def get_work_experience(self) -> int:
        return self.__work_experience

    def get_cars_sold(self) -> [Car]:
        return self.__cars_sold

    def add_sold_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if car not in self.__cars_sold:
            self.__cars_sold.append(car)

    def remove_sold_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if car in self.__cars_sold:
            self.__cars_sold.remove(car)


class Customer:
    def __init__(self, name: str, phone_number: str, mail: str, purchased_cars: [Car] = None) -> None:
        self.__name = name
        self.__phone_number = phone_number
        self.__mail = mail
        self.__purchased_cars = purchased_cars

    def get_name(self) -> str:
        return self.__name

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_mail(self) -> str:
        return self.__mail

    def get_purchased_cars(self) -> [Car]:
        return self.__purchased_cars

    def add_purchased_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if car not in self.__purchased_cars:
            self.__purchased_cars.append(car)

    def remove_purchased_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if car in self.__purchased_cars:
            self.__purchased_cars.remove(car)


class Dealership:
    def __init__(self, cars: [Car] = None, customers: [Customer] = None, salesperson: [Salesperson] = None) -> None:
        self.__cars = cars
        self.__customers = customers
        self.__salesperson = salesperson

    def get_cars(self) -> [Car]:
        return self.__cars

    def get_customers(self) -> [Customer]:
        return self.__customers

    def get_salesperson(self) -> [Salesperson]:
        return self.__salesperson

    def add_car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if car not in self.__cars:
            self.__cars.append(car)
            car.set_status("In stock")

    def sell_car(self, car: Car, salesperson: Salesperson, customer: Customer) -> None:
        if not isinstance(car, Car):
            raise TypeError("Value must be Car")

        if (car in self.__cars) and (customer in self.__salesperson) and (salesperson in self.__salesperson):
            if car.get_status() != "In stock":
                return

            self.__cars.remove(car)
            car.set_status("Sold")
            salesperson.add_sold_car(car)
            customer.add_purchased_car(car)

    def add_salesperson(self, salesperson: Salesperson) -> None:
        if not isinstance(salesperson, Salesperson):
            raise TypeError("Value must be Salesperson")

        if salesperson not in self.__salesperson:
            self.__salesperson.append(salesperson)

    def remove_salesperson(self, salesperson: Salesperson) -> None:
        if not isinstance(salesperson, Salesperson):
            raise TypeError("Value must be Salesperson")

        if salesperson in self.__salesperson:
            self.__salesperson.remove(salesperson)

    def add_customer(self, customer: Customer) -> None:
        if not isinstance(customer, Customer):
            raise TypeError("Value must be Customer")

        if customer not in self.__customers:
            self.__customers.append(customer)


class Program:
    @staticmethod
    def main():
        s1 = Salesperson("FirstS", 5)
        s2 = Salesperson("FirstS", 5)

        cust1 = Customer("FirstC", "+79999999999", "<EMAIL>")
        cust2 = Customer("SecondC", "+71230984567", "<EMAIL>")

        car1 = Car("FirstB", "FirstM", 1999, 5000000.1, "In stock")
        car2 = Car("SecondB", "SecondM", 2010, 6000599.99, "In stock")
        car3 = Car("ThirdB", "ThirdM", 2022, 78901231.85, "In stock")

        dealership = Dealership([car1], [cust1], [s1])

        dealership.add_salesperson(s2)
        dealership.sell_car(car1, s2, cust1)
        print(cust1.get_purchased_cars())

        dealership.add_customer(cust2)
        dealership.add_car(car2)
        dealership.add_car(car3)
        print(dealership.get_cars())

        dealership.sell_car(car2, s2, cust2)
        dealership.sell_car(car3, s1, cust1)


Program.main()

