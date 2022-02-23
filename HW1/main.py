def word_counter():
    """ Функция подсчета количества слов по пробелу """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.read()
        words = book.split()
    return f'Количество слов: {len(words)}'


def avg_word_len():
    """ Функция подсчета средней длинны слова """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.read()
        words = book.split()
    return f'Средняя длинна слова: {sum(len(word) for word in words) / len(words)}'


def alpha_counter():
    """ Функция подсчета количества букв в тексте(кроме пробела) """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.read()
    return f'Количество букв в тексте: {len([alpha for alpha in book if (alpha.isalpha()) and (alpha != " ")])}'


def paragraph_counter():
    """ Функция подсчета количества абзацев в тексте """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.readlines()
        count = 0
        for line in book:
            line = line.split()
            if len(line) > 0:
                count += 1
    return f'Количество абзацев в тексте: {count}'


def top10_words():
    """ Функция подсчета топ-10 самых часто встречаемых слов """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.read().split()
        count_word = []
        index, words = zip(*sorted(enumerate(book), key=lambda word: (-len(word[1]), -word[0]))[:11])
        for i in words:
            x = len(i)
            count_word.append(x)
        return dict(zip(words, count_word))


def top10_alpha():  # лямбда функция работает неверно, сделаю еще один комит с исправлением
    """ Функция подсчета топ-10 самых часто встречаемых букв """
    with open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', 'r') as file:
        book = file.read()
        count_alpha = []
        index, words = zip(*sorted(enumerate(book), key=lambda word: (-len(word[1]), -word[0]))[:11])
        for i in words:
            x = book.count(i)
            count_alpha.append(x)
    return dict(zip(words, count_alpha))


def replace_anna():
    """ Функция замены в тексте слов 'анна павловна' на 'anna pavlovna' """
    file = open('/Users/kreomanser/PycharmProjects/HW1/book2.txt', encoding="utf-8")
    book = file.read()
    file.close()
    newFile = open('/Users/kreomanser/PycharmProjects/HW1/book3.txt', "w", encoding="utf-8")
    newFile.write(book.replace('анна павловна', 'anna pavlovna'))


def replacer(letter, dic):
    """ Функция замены в словаре для последнего задания """
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter


def only_russian_words():
    """
    Функция удаляет все кроме русских букв и сохраняет в новый файл
    Больше похоже на хард код :)
    """
    legend = {
        'a': chr(0),
        'b': chr(0),
        'c': chr(0),
        'd': chr(0),
        'e': chr(0),
        'f': chr(0),
        'g': chr(0),
        'h': chr(0),
        'i': chr(0),
        'j': chr(0),
        'k': chr(0),
        'l': chr(0),
        'm': chr(0),
        'n': chr(0),
        'o': chr(0),
        'p': chr(0),
        'q': chr(0),
        'r': chr(0),
        's': chr(0),
        't': chr(0),
        'u': chr(0),
        'v': chr(0),
        'w': chr(0),
        'x': chr(0),
        'y': chr(0),
        'z': chr(0),
        'A': chr(0),
        'B': chr(0),
        'C': chr(0),
        'D': chr(0),
        'E': chr(0),
        'F': chr(0),
        'G': chr(0),
        'H': chr(0),
        'I': chr(0),
        'J': chr(0),
        'K': chr(0),
        'L': chr(0),
        'M': chr(0),
        'N': chr(0),
        'O': chr(0),
        'P': chr(0),
        'Q': chr(0),
        'R': chr(0),
        'S': chr(0),
        'T': chr(0),
        'U': chr(0),
        'V': chr(0),
        'W': chr(0),
        'X': chr(0),
        'Y': chr(0),
        'Z': chr(0),
        '’': chr(0),
    }
    f_in = open("/Users/kreomanser/PycharmProjects/HW1/book2.txt", encoding="utf-8")
    f_out = open("/Users/kreomanser/PycharmProjects/HW1/book2rus.txt", "wt", encoding="utf-8")
    for line in f_in.read():
        f_out.write(replacer(line, legend))


if __name__ == "__main__":
    print(word_counter())
    print(avg_word_len())
    print(alpha_counter())
    print(paragraph_counter())
    print(top10_words())
    print(top10_alpha())
    only_russian_words()
    replace_anna()
