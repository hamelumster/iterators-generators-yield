class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        # Создаем стек для хранения элементов, которые нужно обработать
        self.stack = []
        # Инициализируем стек начальным списком
        self._flatten(self.list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        # Если стек пуст, значит, все элементы обработаны
        if not self.stack:
            raise StopIteration
        # Извлекаем следующий элемент из стека
        return self.stack.pop(0)

    def _flatten(self, items):
        # Рекурсивный метод для разворачивания списка
        for item in items:
            if isinstance(item, list):
                # Если элемент является списком, рекурсивно обрабатываем его
                self._flatten(item)
            else:
            # Если элемент не является списком, добавляем его в стек
                self.stack.append(item)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()