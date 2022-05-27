class MyList:
    data = []
    default_type = type

    def __init__(self, data=None):
        if type(data) in (float, int, None):
            default_type = type(data)
            self.data.append(data)
        else:
            assert NotImplemented

    def __iter__(self):
        for elem in self.data:
            yield elem

    def get(self, copy=True):
        if copy:
            new_list = MyList()
            return new_list
        else:
            return self.data

    def add_end(self, *element):
        if type(element) in [list, MyList]:
            self.data += element
        elif len(element) == 1:
            elem = element[0]
            new = self.default_type(elem)
            self.data.append(new(elem))
        else:
            assert ValueError

    def add_begin(self, *element):
        if type(element) in (list, MyList):
            index = 0
            for elem in range(element):
                index += 1
                new = self.default_type(elem)
                self.data.insert(index, new(elem))
        elif len(element) == 1:
            elem = element[0]
            new = self.default_type(elem)
            self.data.insert(0, new(elem))
        else:
            assert ValueError

    def __str__(self):
        return self.data

    # def full_convert(self, _type):
    #     if type(_type) in (dict, set, tuple, list):
    #         pass


if __name__ == "__main__":
    l = MyList(7.0)
    l.get()
    print(*l)
