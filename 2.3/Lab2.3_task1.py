class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Использует setter для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("pages должен быть целым числом")  # Ошибка типа
        if value <= 0:
            raise ValueError("pages должен быть положительным целым числом")  # Ошибка значения
        self._pages = value



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Использует setter для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):  # Проверка типа (float или int)
            raise TypeError("duration должен быть числом с плавающей точкой")
        if value <= 0:
            raise ValueError("duration должен быть положительным числом с плавающей точкой")
        self._duration = float(value)  # Приведение к float


# Примеры использования
pb = PaperBook("1984", "Джордж Оруэлл", 328)
ab = AudioBook("1984", "Джордж Оруэлл", 11.5)

print(pb)
print(repr(pb))

print(ab)
print(repr(ab))
