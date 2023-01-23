from abc import ABC, abstractmethod



class I__Model(ABC):
    """    Абстрактный интерфейсный класс с абстрактными методами.
    Описывает интерфейс - поведение модели расчетов"""

    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def set_x(self, value):
        pass

    @abstractmethod
    def set_y(self, value):
        pass
