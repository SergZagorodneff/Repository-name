class Guitar:
    """
    Базовый класс для всех гитар.
    brand (str): производитель гитары.
    model (str): модель гитары.
    num_strings (int): количество струн (по умолчанию 6).
    """

    def __init__(self, brand: str, model: str, num_strings: int = 6):
        """
        :param brand: производитель гитары.
        :param model: модель гитары.
        :param num_strings: количество струн (по умолчанию 6).
        """
        self.brand = brand
        self.model = model
        self.num_strings = num_strings

    def __str__(self) -> str:
        """Выводит строковое представление гитары."""
        return f"{self.brand} {self.model} ({self.num_strings} струн)"

    def __repr__(self) -> str:
        """Выводит формальное строковое представление объекта."""
        return f"Guitar(brand={self.brand!r}, model={self.model!r}, num_strings={self.num_strings!r})"

    def play(self) -> str:
        """
        Метод для игры на гитаре.
        :return: Строка с описанием звука.
        """
        return "Звук гитары."

class ElectricGuitar(Guitar):
    """
    Дочерний класс для электрических гитар.
    brand (str): производитель гитары.
    model (str): модель гитары.
    num_strings (int): количество струн (по умолчанию 6).
    pickup_type (str): тип звукоснимателя (например, "сингл" или "хамбакер").
    """

    def __init__(self, brand: str, model: str, pickup_type: str, num_strings: int = 6):
        """
        :param brand: производитель гитары.
        :param model: модель гитары.
        :param pickup_type: тип звукоснимателя.
        :param num_strings: количество струн (по умолчанию 6).
        """
        super().__init__(brand, model, num_strings)
        self.pickup_type = pickup_type

    def __str__(self) -> str:
        """Выводит строковое представление электрической гитары."""
        return f"{self.brand} {self.model} ({self.pickup_type}, {self.num_strings} струн)"

    def __repr__(self) -> str:
        """Выводит формальное строковое представление объекта."""
        return f"ElectricGuitar(brand={self.brand!r}, model={self.model!r}, pickup_type={self.pickup_type!r}, num_strings={self.num_strings!r})"

    def play(self, distortion: bool = False) -> str:
        """
        Перегруженный метод для игры на электрической гитаре: добавляет возможность использования эффекта дисторшн.
        :param distortion: включить дисторшн (по умолчанию False).
        :return: строка с описанием звука.
        """
        if distortion:
            return "Мощный звук с дисторшном!"
        return "Чистый звук электрической гитары."

class AcousticGuitar(Guitar):
    """
    Дочерний класс для акустических гитар.
    brand (str): Производитель гитары.
    model (str): Модель гитары.
    num_strings (int): Количество струн (по умолчанию 6).
    body_type (str): Тип корпуса (например, "дредноут").
    """

    def __init__(self, brand: str, model: str, body_type: str, num_strings: int = 6):
        """
        Конструктор дочернего класса.
        :param brand: производитель гитары.
        :param model: модель гитары.
        :param body_type: тип корпуса (например, "дредноут").
        :param num_strings: количество струн (по умолчанию 6).
        """
        super().__init__(brand, model, num_strings)
        self.body_type = body_type

    def __str__(self) -> str:
        """Выводит строковое представление акустической гитары."""
        return f"{self.brand} {self.model} ({self.body_type}, {self.num_strings} струн)"

    def __repr__(self) -> str:
        """Выводит формальное строковое представление объекта."""
        return f"AcousticGuitar(brand={self.brand!r}, model={self.model!r}, body_type={self.body_type!r}, num_strings={self.num_strings!r})"

    def play(self) -> str:
        """
        Перегруженный метод для игры на акустической гитаре: добавляет специфичное описание звука.
        :return: Строка с описанием звука.
        """
        return "Теплый и насыщенный звук акустической гитары."

if __name__ == "__main__":

    pass