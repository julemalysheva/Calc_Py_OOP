from abc import ABC, abstractmethod


class I__View(ABC):
    """    Абстрактный интерфейсный класс с абстрактными методами.
    Описывает интерфейс - поведение при взаимодействии с пользователем"""

    @abstractmethod
    def get_variant(self, title):
        pass

    @abstractmethod
    def get_value(self, title):
        pass

    @abstractmethod
    def view_data(self, data, title):
        pass

    @abstractmethod
    def view_logger(self, fl):
        pass
