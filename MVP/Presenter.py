from MVP.Models.DivModel import DivModel
from MVP.Models.MulModel import MulModel
from MVP.Models.SubModel import SubModel
from MVP.Models.SumModel import SumModel


class Presenter:
    """Класс описывает компоненту связи Model и View между собой.
     Константа TITLE_GET_VALUE содержит повторяющуюся строку запроса числа,
     константа-словарь DICT_OPERATION используется для форматированного пользовательского вывода.
     При инициализации принимает тип пользовательского интерфейса - дочерний класс интерфейса I__View.
     Модель расчета устанавливается в зависимости от выбранной операции."""

    TITLE_GET_VALUE: str = '''
            1. В рациональных числах используйте точку (.) 
            - например: 2.54; 1.05; 6.45 и т.п.
            2. В комплексных числах используйте j 
            - например: (2+4j); (1-3j); (1+8j) и т.п.
            👉 Введите значение: '''

    DICT_OPERATION = {1: '+', 2: '-', 3: '*', 4: '/'}

    def __init__(self, view):
        self.__model = None
        self.__view = view

    def __set_model(self, variant):
        """Метод устанавливает конкретный тип / подкласс  модели расчета, с которой будет работать
        текущая компонента управления связями - в зависимости от пользовательского выбора операции"""

        if variant == 1: self.__model = SumModel()
        elif variant == 2: self.__model = SubModel()
        elif variant == 3: self.__model = MulModel()
        elif variant == 4: self.__model = DivModel()


    def button_click(self):
        """Метод запуска текущей компоненты управления связями"""

        first_number = self.__view.get_value(self.TITLE_GET_VALUE)
        while True:
            operation = self.__view.get_variant(""" 
                    Выберите операцию - введите число пункта меню:
                        1 - сложить (+)
                        2 - вычесть (-)
                        3 - умножить (*)
                        4 - разделить (/)
                    """)
            if 1 <= operation <= 4:
                break
        second_number = self.__view.get_value(self.TITLE_GET_VALUE)
#         дальше устанавливаем Model в зависимости от операции
        self.__set_model(operation)
        self.__model.set_x(first_number)
        self.__model.set_y(second_number)
        res = self.__model.result()
        if res != None:
            self.__view.view_data(res, f'{first_number} {self.DICT_OPERATION[operation]} {second_number}')
        else:
            self.__view.view_data(res, f'Деление на --0--! {first_number} {self.DICT_OPERATION[operation]}'
                                       f' {second_number}')

