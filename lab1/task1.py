# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


from abc import ABC, abstractmethod
import doctest

class Bee(ABC):

    def __init__(self, species: str, wingspan: float):

        if not isinstance(species, str):
            raise TypeError("Вид пчелы должен быть строкой.")
        if not isinstance(wingspan, (int, float)) or wingspan <= 0:
            raise ValueError("Размах крыльев должен быть положительным числом.")

        self.species = species
        self.wingspan = wingspan

    @abstractmethod
    def collect_nectar(self, flowers: int) -> float:
        """
        Сбор нектара с цветов.
        :param flowers: Количество цветов, с которых собирать нектар (должно быть >= 1).
        :return: Количество собранного нектара в миллилитрах.
        """


    @abstractmethod
    def produce_honey(self) -> float:
        """
        Производство меда из собранного нектара.
        :return: Количество произведенного меда в граммах.
        """



class Car(ABC):

    def __init__(self, brand: str, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Машина"
        :param brand: Марка автомобиля.
        :param fuel_capacity: Емкость бака в литрах (должна быть > 0).
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой.")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Емкость бака должна быть положительным числом.")

        self.brand = brand
        self.fuel_capacity = fuel_capacity

    @abstractmethod
    def drive(self, distance: float) -> float:
        """
        Движение автомобиля на указанное расстояние.
        :param distance: Расстояние в километрах (должно быть >= 0).
        :return: Оставшееся количество топлива в литрах.
        """


    @abstractmethod
    def refuel(self, fuel: float) -> None:
        """
        Заправка автомобиля.
        :param fuel: Количество топлива в литрах (должно быть > 0).
        """



class Chair(ABC):


    def __init__(self, material: str, max_weight: float):
        """
        Создание и подготовка к работе объекта "Стул"
        :param material: Материал стула (например, дерево, пластик).
        :param max_weight: Максимальная допустимая нагрузка в килограммах (должна быть > 0).
        """
        if not isinstance(material, str):
            raise TypeError("Материал стула должен быть строкой.")
        if not isinstance(max_weight, (int, float)) or max_weight <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительным числом.")

        self.material = material
        self.max_weight = max_weight

    @abstractmethod
    def sit(self, weight: float) -> bool:
        """
        Проверка, выдержит ли стул человека с указанным весом.
        :param weight: Вес человека в килограммах (должен быть > 0).
        :return: True, если вес допустим, иначе False.
        """

    @abstractmethod
    def move(self, distance: float) -> None:
        """
        Перемещение стула на указанное расстояние.
        :param distance: Расстояние в метрах (должно быть >= 0).
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации