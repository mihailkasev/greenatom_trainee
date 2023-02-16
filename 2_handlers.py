# В представленном фрагменте кода в lambda выражении передана функция с аргументом в ней, которым является внешняя переменная step из цикла for, 
# соответственно при вызове обработчика данная переменная будет каждый раз принимать последнее значение, а именно 4.
# Необходимо, чтобы метод create_handlers возвращал сгенерированный список функций, который бы передавался в execute_handlers. Данный метод вызывает функции 
from typing import Callable


def create_handlers(callback: Callable[[int], int]) -> list:
    """Возвращает сгенерированный список обработчиков в заданном диапазоне"""
    return [callback for _ in range(5)]

def execute_handlers(handlers: list):
    """ Запускает добавленные обработчики (от 0 до 4) """
    for index, handler in enumerate(handlers):
        handler(index)
