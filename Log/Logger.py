from datetime import datetime as dt


class Logger:
    """ класс для логирования работы программы - содержит статические методы."""

    @staticmethod
    def menu_logger(data):
        """    записываем в лог выбранный вариант меню с указанием даты/времени"""

        with open("log.txt", 'a', encoding="utf8") as file:
            file.write('{} Выбран пункт меню {}\n'
                       .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))

    @staticmethod
    def input_logger(data):
        """    записываем в лог введенное значение для расчета с указанием даты/времени"""

        with open("log.txt", 'a', encoding="utf8") as file:
            file.write('{} Введено значение {}\n'
                       .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))

    @staticmethod
    def error_logger(data):
        """    записываем в лог ошибку с указанием даты/времени - аргумент data будет передаваться на стороне view
    на этапе обработки - здесь  просто фиксация"""

        with open("log.txt", 'a', encoding="utf8") as file:
            file.write('{} Зафиксирована ошибка {}\n'
                       .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))

    @staticmethod
    def res_logger(data):
        """    записываем в лог выдачу результата - аргумент data будет передаваться на стороне view"""

        with open("log.txt", 'a', encoding="utf8") as file:
            file.write('{} Получен результат вычисления {}\n'
                       .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))

    @staticmethod
    def view_log_logger(data):
        """    записываем в лог показ файла лог - сама выдача будет описана на стороне view
    здесь фиксируем это событие"""

        with open("log.txt", 'a', encoding="utf8") as file:
            file.write('{} Выдан файл лога по запросу {}\n'
                       .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
