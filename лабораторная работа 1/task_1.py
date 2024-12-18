# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Car:
    def __init__(self, weight: int, wheels: int):
        """
        Создание и подготовка к работе объекта "Легковая машина"

        :param weight: Вес машины
        :param wheels: Количество колес у машины

        Примеры:
        >>> car = Car(2500, 4)
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

        if not isinstance(wheels, int):
            raise TypeError("Количество колес должно быть типа int")
        if wheels <= 0:
            raise ValueError("Количество колес должно быть положительным числом")
        self.wheels = wheels

    def is_car_light(self) -> bool:
        """
        Функция проверяет не превышает ли машина максимальный вес легковой машины

        :return: Превышает ли машина максимальный вес легковой машины

        Примеры:
        >>> car = Car(4000, 4)
        >>> car.is_car_light()
        """
        ...

    def add_seats_to_car(self, seats: int):
        """
        Добавление сидений в машину.
        :param seats: Количество добавляемых сидений

        :raise ValueError: Если количество добавляемых сидений превышает максимально разрешенное, то вызываем ошибку

        Примеры:
        >>> car = Car(2500, 4)
        >>> car.add_seats_to_car(2)
        """
        if not isinstance(seats, int):
            raise TypeError("количество добавляемых сидений должно быть типа int")
        if seats < 0:
            raise ValueError("количество добавляемых сидений должно быть положительным числом")
        ...


class BoxWithToys:
    def __init__(self, volume: int, already_toys: int):
        """
        Создание и подготовка к работе объекта "Коробка с игрушками"

        :param volume: Объем коробки
        :param already_toys: Количество игрушек

        Примеры:
        >>> box_with_toys = BoxWithToys(1500, 6)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.volume = volume

        if not isinstance(already_toys, int):
            raise TypeError("Количество игрушек должно быть типа int")
        if already_toys <= 0:
            raise ValueError("Количество игрушек должно быть положительным числом")
        self.already_toys = already_toys
    def add_toys_to_box(self, more_toys: int):
        """
        Добавление игрушек в коробку.
        :param more_toys: Количество добавляемых игрушек


        Примеры:
        >>> box_with_toys = BoxWithToys(1500, 6)
        >>> box_with_toys.add_toys_to_box(4)
        """
        if not isinstance(more_toys, int):
            raise TypeError("количество добавляемых игрушек должно быть типа int")
        if more_toys < 0:
            raise ValueError("количество добавляемых игрушек должно быть положительным числом")
        ...

class Table:
    def __init__(self, length: int, width: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param width: Ширина стола

        Примеры:
        >>> table = Table(120, 80)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

    def is_table_square(self) -> bool:
        """
        Функция проверяет является ли стол квадратным

        :return: Является ли стол квадратным

        Примеры:
        >>> table = Table(120, 120)
        >>> table.is_table_square()
        """

        ...

    def is_table_rectangular(self) -> bool:
        """
        Функция проверяет является ли стол прямоугольным

        :return: Является ли стол прямоугольным

        Примеры:
        >>> table = table(500, 0)
        >>> table.is_table_rectangular()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
