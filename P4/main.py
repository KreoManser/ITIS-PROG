"""
# написать функцию def choose(obj), которая при получении tuple вернет произведение элементов,
# если list то вернет сумму элементов
# eсли dict то поменяет ключи и значения местами (ключи и значения уникальны)
# если это set то вернуть множество где элементы возведены в квадрат
# если это число (int, float) то просто вернуть его
from functools import reduce


def choose(obj):
    if type(obj) == tuple:
        return reduce(lambda x, y: x * y, obj)
    elif type(obj) == list:
        return sum(obj)
    elif type(obj) == dict:
        return dict(zip(obj.values(), obj.keys()))
    elif type(obj) == set:
        return set(map(lambda x: x * x, obj))
    elif type(obj) == (int or float or complex):
        return obj
    else:
        raise Exception("Warning!")


if __name__ == "__main__":
    tuple_ = (1, 5, 3, 2, 1)
    array = [1, 5, 3, 2, 1]
    mydict = {1: "2", 2: '7', 3: '5'}
    myset = {1, 6, 4, 2, 1}

    print(choose(tuple_))
"""
# OOP


class Human:
    def __init__(self, name):
        self.__height = 170
        self.__weight = 70
        self.name = name

    def __repr__(self):
        return f"{self.name}. Рост: {self.__height} Вес: {self.__weight}"

    # def __str__(self):  # НЕ РАБОТАЕТ С КОЛЛЕКЦИЯМИ!
    #     return f"{self.name}. Рост: {self.__height} Вес: {self.__weight}"

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if 30 < new_height < 200:
            self.__height = new_height
        return self.__height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 30 < value < 200:
            self.__height = value


if __name__ == "__main__":
    Vasya = Human("Vasya")
    print(Vasya.get_height())
    print(Vasya.height)
    print(Vasya.set_height(190))
    # Vasya.height = 170
    class_room = [Human(name) for name in "ABCDEFGHKLM"]
    print(class_room)