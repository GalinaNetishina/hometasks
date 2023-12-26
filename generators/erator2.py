import types
from itertools import chain


def flat_generator(list_of_lists):
    for item in list_of_lists:
        current_list = iter(item)
        for el in current_list:
            yield el

def flat_generator_v1(list_of_lists):
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item


def flat_generator_v2(list_of_lists):
    for inner_list in list_of_lists:
        yield from inner_list


def flat_generator_v3(list_of_lists):
    for item in chain.from_iterable(list_of_lists):
        yield item


def flat_generator_v4(list_of_lists):
    return (item for item in chain.from_iterable(list_of_lists))


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    