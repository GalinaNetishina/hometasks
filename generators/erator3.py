class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.stack = []
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_of_lists):
            if self.stack:
                self.list_of_lists, self.index = self.stack.pop()
                return next(self)
            raise StopIteration
        element = self.list_of_lists[self.index]
        self.index += 1
        if type(element) is not list:
            return element
        self.stack.append((self.list_of_lists, self.index))
        self.list_of_lists = element
        self.index = 0
        return next(self)

class FlatIteratorHard:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iters_stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        while self.iters_stack:
            try:
                next_item = next(self.iters_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iters_stack.pop()
                #  если не получилось, значит итератор пустой
                continue

            if isinstance(next_item, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iters_stack.append(iter(next_item))

            else:
                return next_item
        raise StopIteration


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
        print(flat_iterator_item, end=' ')
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
    