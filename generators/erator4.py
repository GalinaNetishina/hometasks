import types
from itertools import chain



def flat_generator(list_of_list):
    is_flat = lambda x: not isinstance(x,list)
    for i in list_of_list:
        if is_flat(i):
            yield i
        else:
            yield from flat_generator(i)

def flat_generator_v5(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            for j in flat_generator_v5(i):
                yield j
        else:
            yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item, end=' ')
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
