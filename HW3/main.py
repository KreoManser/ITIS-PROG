def f1(a, b):
    return sorted(a) == sorted(b)


def f2(a, b):
    return a + b


def f3(test_list, d):
    return tuple([elem for elem in test_list if elem >= d]), [elems for elems in test_list if elems < d]


def f4(test_list):
    return test_list[::-1] == test_list


def f5(test_list):
    return [index for index in test_list if index != 0]


def f6(test_list, d):
    return min(test_list, key=lambda x: abs(x - d))


def f7(test_list):
    test_list_max = []
    max_ = test_list[0]
    i = 0
    while i + 2 < len(test_list):
        if (test_list[i] + test_list[i + 1] + test_list[i + 2] > max_):
            max_ = test_list[i] + test_list[i + 1] + test_list[i + 2]
            test_list_max = [test_list[i], test_list[i + 1], test_list[i + 2]]
        i += 1
    return test_list_max


def f8(test_list):
    if len(test_list) % 2 == 0:
        del test_list[len(test_list)//2]
        del test_list[round(len(test_list) // 2)]
    if len(test_list) % 2 == 1:
        del test_list[round(len(test_list) // 2)]
    return test_list


def f9(test: int) -> str:
    stroke_list = []
    i = 1
    while test > 0:
        stroke_list.append(test % 10 * i)
        test //= 10
        i *= 10
    stroke = " + ".join(str(num) for num in stroke_list[::-1])
    return stroke


def f10(l):
    x = round(len(l) / 3) + 1
    return tuple(l[:x]), tuple(l[x:x*2]), tuple(l[x*2:])


if __name__ == "__main__":
    print(f'F1: {f1([1, 4, 3, 1, 1], [4, 1, 1, 1, 3])}')
    print(f'F2: {f2((1, 1), (4, 4, 4))}')
    test_list = [0, 4, 6, 8, 1, -9, 0, 1, 2, 1, 7, 0]
    ans1, ans2 = f3(test_list, 4)
    print(f'F3: {ans1, ans2}')
    print(f'F4: {f4(test_list)}')
    print(f'F5: {f5(test_list)}')
    print(f'F6: {f6(test_list, (-10.4))}')
    print(f'F7: {f7(test_list)}')
    print(f'F8: {f8(test_list)}')
    print(f'F9: {f9(1234)}')
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'F10: {f10(test_list)}')
    print(round(10 / 3))