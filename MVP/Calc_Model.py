from MVP.I__Model import I__Model
from abc import ABC, abstractmethod


class Calc_Model(I__Model, ABC):
    """    Абстрактный класс Calc_Model (наследуется от интерфейсного абстр.класса I__Model) - Модель расчета
    - содержит атрибуты x и y, которые участвуют в расчетах.
    Методы set_x и set_y реализованы в классе, т.е. не обязательны для переопределения в наследниках,
    т.к. являются однотипными для дочерних"""

    def __init__(self):
        self.y = None
        self.x = None

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value



