def reverse(number):
    if isinstance(number, int):
        return int(str(number)[::-1])
    if isinstance(number, float):
        return float(str(number)[::-1])


def no_dup(mydict):
    values = []
    keys = []
    Set_ = set()
    for (key, value) in mydict.items():
        if value in Set_:
            continue
        else:
            Set_.add(value)
            values.append(value)
            keys.append(key)
    return dict(zip(keys, values))


def summarize(number):
    number = number
    result = 0
    result_one = 10
    while len(str(result_one)) != 1:
        while number > 0:
            result += number % 10
            number //= 10
        number = result
        result_one = result
        result = 0
    return result_one


def brick_lang(string):
    alph = ["и", "е", "а"]
    new = ""
    for i in range(len(string)):
        if string[i] in alph:
            new += "к" + string[i]
        else:
            new += string[i]
    return string


if __name__ == "__main__":
    print(f'Task 1: {reverse(185)}')
    print(f'Task 1: {reverse(14.815162342)}')
    mydict_ = {2: 9, 5: -3, 3: 3, 7: 3, 4: 20, 1: 9, 6: 9, 11: 3, 13: 6}
    print(f'Task 2: {no_dup(mydict_)}')
    print(f'Task 3: {summarize(156)}')
    mystr = "Привееет! Как Дела?"
    print(f'Task 4: {brick_lang(mystr)}')
