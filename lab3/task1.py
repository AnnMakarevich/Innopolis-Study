class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self, value: str):
        raise AttributeError("Название книги нельзя изменить.")

    def author(self) -> str:
        return self._author

    def author(self, value: str):
        raise AttributeError("Автора книги нельзя изменить.")

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"
    #
    # def __repr__(self):
    #     return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self._pages = pages
        super().__init__(name, author)

    def pages(self) -> int:
        return self._pages

    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} (количество страниц: {self.pages})"

    def __repr__(self) -> str:
        return f"{super().__repr__()[:-1]}, pages={self.pages})"
    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"

class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        self._duration = duration
        super().__init__(name, author)

    def duration(self, value: float):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:
        return f"{super().__str__()} (продолжительность: {self.duration:.2f} часов)"

    def __repr__(self) -> str:
        return f"{super().__repr__()[:-1]}, duration={self.duration:.2f})"
