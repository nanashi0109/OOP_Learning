from math import sqrt


# region Task_1
def quadratic_equation() -> None:
    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0")
    a = int(input("Коэффициент a: "))
    b = int(input("Коэффициент b: "))
    c = int(input("Коэффициент c: "))

    discriminant = b*b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        print(f"Корни уравнения: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Корень уравнения: {root}")
    elif discriminant < 0:
        print("У уравнения нет действительных корней")
# endregion


# region Task_2
def triangle_area() -> None:
    print("Введите длины сторон треугольника a, b и c:")
    a = int(input("Сторона a: "))
    b = int(input("Сторона b: "))
    c = int(input("Сторона c: "))

    if(a + b <= c) or (a + c <= b) or (b+c <= a):
        return

    half_perimetr = (a + b + c) / 2
    area = sqrt(half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))
    print(f"Площадь треугольника {area}")
# endregion


# region Task_3
def temperature_conversion():
    print("Выберите опцию: ")
    print("1. Конвертировать Цельсий в Фаренгейт")
    print("2. Конвертировать Фаренгейт в Цельсий")
    choice = int(input())

    if choice == 1:
        print("Введите температуру в градусах Цельсия:")
        celsius = int(input())
        fahrenheit = (celsius * 9.0/5.0) + 32
        print(f"Температура в градусах Фаренгейта: {fahrenheit}")

    elif choice == 2:
        fahrenheit = int(input("Введите температуру в градусах Фаренгейта:"))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"Температура в градусах Цельсия: {celsius}")
    else:
        print("Неправильный выбор")
# endregion


class Program:
    @staticmethod
    def main():
        quadratic_equation()
        triangle_area()
        temperature_conversion()


Program.main()
