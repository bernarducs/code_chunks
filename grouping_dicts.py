from itertools import groupby

lista = [
        {'a': 1}, {'a': 5}, {'a': 3}, {'b': 2}, {'b': 9}
    ]

for key, group in groupby(lista, lambda key: list(key)):
    print('{}: {}'.format(key[0], [i[key[0]] for i in group]))