from itertools import chain


class FlatIterator:

    def __init__(self, list_of_list):
        self.list = []
        for i in list_of_list:
            self.list.extend(i)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.list):
            raise StopIteration
        i = self.cursor
        self.cursor += 1
        return self.list[i]


class FlatIteratorV1:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_inner = -1
        self.cursor_outer = 0
        return self

    def __next__(self):
        self.cursor_inner += 1
        if self.cursor_inner >= len(self.list_of_list[self.cursor_outer]):
            self.cursor_outer += 1
            self.cursor_inner = 0
        if self.cursor_outer >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.cursor_outer][self.cursor_inner]


class FlatIteratorV2:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iterators = iter(iter(l) for l in self.list_of_list)
        self.current_iter = next(self.iterators)
        return self

    def __next__(self):
        try:
            next_item = next(self.current_iter)
        except StopIteration:
            self.current_iter = next(self.iterators)
            next_item = next(self.current_iter)
        return next_item


class FlatIteratorV3:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_iter = chain.from_iterable(self.list_of_list)
        return self

    def __next__(self):
        return next(self.flat_iter)


class FlatIteratorV4:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        return chain.from_iterable(self.list_of_list)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIteratorV1(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIteratorV1(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
