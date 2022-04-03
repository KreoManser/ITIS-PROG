# Дачник
class Raspberry:
    states = {
        1: "None",
        2: "Bloom",
        3: "Green",
        4: "Red"
    }
    # state = list(states.values())[0]  # почка

    def __init__(self, _index, _state=1):
        """
        :param _index: Index raspberry.
        :param _state: Maturity stage.
        """
        self._index = _index
        self._state = _state

    def grow(self):
        """
        :return: Phase growth.
        """
        try:
            if (self._state >= 0) and (self._state < len(self.states)):
                self._state += 1
            return list(self.states.values())[self._state]
        except IndexError:
            return f'Warning: ripe!'

    def is_ripe(self):
        """
        :print: Finished maturity stage.
        """
        if self._state == int(list(self.states.keys())[len(self.states) - 1]):
            return f'Ripe!'

    def __repr__(self):
        """
        :return: index - Raspberry, phase growth
        :P.S: (self._state - 1) - starting phase in __init__ = 0(for stable work func - is_ripe)
        """
        return f'index: {self._index}, phase growth: {list(self.states.values())[self._state - 1]}'


class RaspberryBush:
    # raspberries = [Raspberry(f"Ягода_{i}") for i in range(20)]
    raspberries = {}

    def __init__(self, count):
        """
        :param count: Init count of raspberry.
        """
        self.count = count
        self.raspberries = {i: i for i in range(count+1)}

    def grow_all(self):
        # for i in range(0, len(self.raspberries)):
            # Raspberry_in = Raspberry(i)
            # self.raspberries.append(Raspberry(i).grow())
            # print(self.raspberries)
        return self.raspberries

    def __repr__(self):
        return f'count: {self.count}, raspberries: {self.raspberries}'


if __name__ == "__main__":
    # Raspberry1 = Raspberry(1)
    # print(Raspberry1)
    # print(Raspberry1.grow())
    # print(Raspberry1.grow())
    # print(Raspberry1.grow())
    # print(Raspberry1.is_ripe())
    RaspberryBush1 = RaspberryBush(4)
    print(RaspberryBush1)
    print(RaspberryBush1.grow_all())
    # print(Raspberry1)
    # states = {
    #     1: "Bud",
    #     2: "Leaves",
    #     3: "Formations",
    #     4: "Raspberry"
    # }
    # state = (list(states.values())[0])
    # print(type(state))
    # for i in range(3):
    #     print(Raspberry(1, 0).grow(i))
