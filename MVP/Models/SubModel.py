from MVP.Calc_Model import Calc_Model


class SubModel(Calc_Model):
    """Класс выполняет операцию вычитания с заданными числами.
    Наследуется от абстрактного класса Calc_Model, который в свою очередь наследует интерфейсный
    абстрактный класс I__Model"""

    def __init__(self):
        super().__init__()

    def result(self):
        """Метод возвращает результат вычислений 2х чисел"""

        return self.x - self.y

