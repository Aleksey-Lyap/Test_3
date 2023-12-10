# Вопрос №1
"""Функции для определения четности числа.

Плюсы: читаемость, простота, алгоритмическая сложность О(1).

"""
def isEven(value):

      return value % 2 == 0

def is_Odd(value):

      return value % 2 != 0




# Вопрос №2

class FIFO:
    """Способ реализации FIFO через list.

    Плюсы: простота, читаемость, алгоритмическая сложность О(1).

    Минусы: избыточность данных, нарушение порядка, проблемы с пустыми элементами.

    """
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def add_queue(self, item):
        self.items.append(item)
        if self.tail == len(self.items) - 1:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = self.head + 1
        return item
    

class FIFO:
    """Способ реализации FIFO через словарь.

    Плюсы: читаемость, алгоритмическая сложность О(1),
    отсутствие избыточности данных.

    Минусы: проблемы с ключами, ограничения словарей.

    """
    def __init__(self):
        self.items = {}
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, item):
        self.items[self.tail] = item
        if self.tail == len(self.items) - 1:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Очередь пуста')
        item = self.items.pop(self.head)
        self.head = self.head + 1
        return item





# Вопрос №3

def merge_sort(arr):
    """Функция представляет сортировку слиянием.

    Эффективная - алгоритмическая сложность О(n*lon(n)).

    Скорость сортировки не измениться в отсортированом массиве.

    Стабильная - порядок равных элементов сохраниться.

    Нуждается в дополнительной памяти.

    """
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
