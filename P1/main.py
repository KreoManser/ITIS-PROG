from copy import deepcopy
from time import time as t
import numpy as np


def measure(func):
    def wrapper(*args, **kwargs):
        start = t()
        res = func(*args, **kwargs)
        end = t()
        print(f'time: {end - start}')
        return res
    return wrapper


"""
def _any(array):  # all принмиает на вход список из любых элементов и возвращает
    # True если все элементы True, иначе False
    for elem in array:
        if elem:
            return True
    return False


def _all(array):  # any, возвращает True если хотя бы один элемнет True
    counter = 0
    for elem in array:
        if not elem:
            counter += 1
    if counter == len(array):
        return True
    return False



def transponse(matrix):
    return list(map(list, zip(*matrix)))



def transponse2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0] * rows for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix
"""


@measure
def k1(m):
    return [row.copy() for row in m]


@measure
def k2(m):
    return [row[:] for row in m]


@measure
def k3(m):
    return deepcopy(m)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 5]
    b = [4, 5, 3, 6, 7, 9]
    c = []

    for i in a:
        if i in b:
            c.append(i)

    print(c)
    """
    m = np.random.uniform(-100, 100, size=(14000, 14000))
    print(k1(m))
    print(k2(m))
    k3(m)

    a = [[1, 2], [3, 4]]
    b = [row.copy() for row in a]
    b[0][0] = None
    print(a)
    print(b)
    
    rows = 1800
    cols = 2200
    m = np.random.uniform(-100, 100, rows * cols).reshape(rows, cols)
    l = max(max(row) for row in m)  # быстрее чем с [генератором]
    l1 = np.max(np.asarray(m, dtype=int))
    print(l, l1)

    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    b_zipped = zip(*a)
    transpose = [list(row) for row in b_zipped]
    print(transpose)

    a = [1, 2, 3, 4, 5]
    b = [3, 5, 6, 1, 3]
    c = [1, 1, 1, 1, 1]

    # 1
    for i in range(len(a)):
        x = a[i] ** b[i] - c[i]
        print(x)
    # 2
    for i in zip(a, b, c):
        t = a ** b - c
        print(t)
    """
    