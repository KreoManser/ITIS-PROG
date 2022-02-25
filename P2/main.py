"""
Смержить два списка получив пару значений у ключа


def merge(*dictionaries):
    res = dictionaries[0].copy()
    for d in dictionaries[1:]:
        for key, value in d.items():
            if key not in res:
                res[key] = value
            else:
                if isinstance(res[key], list):
                    res[key].append(value)
                else:
                    res[key] = [res[key], value]
    return res


if __name__ == "__main__":
    a = {1: 1, 2: 2, 3: 3}
    b = {1: 31, 4: 2, 3: "None"}

    # c = {
    #     1: [1, 31],
    #     2: 2,
    #     3: [3, "None"],
    #     4: 2
    # }
    print(merge(a, b))



if __name__ == "__main__":
    #  Реализация стэка/очереди
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack.pop)  # - СТЭК
    print(stack.pop(0))  # - ОЧЕРЕДЬ
    print(stack)
    #  Реализция очереди
"""
import math
# from collections import namedtuple
# 1
# Point = namedtuple('Point', [x, y, s])
# p = Point(11, y=22, s=30)
# from typing import NamedTuple
#
# 2
# class Layout(NamedTuple):
#     x: float
#     y: float
#     s: float

# 3
class Point:
    def __init__(self, x, y, s):
        self.__x = x
        self.__y = y
        self.__s = s

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def s(self):
        return self.__s


def read_data():
    # dx, dy = [], []
    with open("/Users/kreomanser/PycharmProjects/P2/buildings.txt", "r") as file:
        data = {}
        for line in file:
            address, *raw = line.strip().split('\t')
            data[address] = Point(*tuple(map(float, raw)))
    return data


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def maxMinDist():
    for i in range
    pass
    return


if __name__ == "__main__":
    data_ = read_data()
    point1 = list(data_.keys())[9]
    point2 = list(data_.keys())[18]
    p1 = data_[point1]
    p2 = data_[point2]
    print(data_)
    print(point1)
    print(point2)
    print(distance(p1.x, p1.y, p2.x, p2.y))
