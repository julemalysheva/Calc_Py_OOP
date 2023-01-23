"""Модуль запуска приложения - точка входа

создаем экземпляр пользовательского интерфейса
view = Console_View()

создаем экземпяяр компоненты управления связью между интерфейсом и моделью расчета
presenter = Presenter(view)

создаем экземпляр приложения для запуска меню
app = App(presenter, view)

запускаем приложение с заданными параметрами
app.start()
"""

from App import App
from Console_View import Console_View
from MVP.Presenter import Presenter

view = Console_View()
presenter = Presenter(view)
app = App(presenter, view)
app.start()


