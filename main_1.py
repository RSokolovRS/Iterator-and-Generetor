# Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и
# возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.

import types


def flat_generator(list_of_lists):
    counter = 0
    result = sum(list_of_lists, [])
    yield from [r for r in result if len(result)> counter]
    counter += 1

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