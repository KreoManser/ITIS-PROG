"""
Если надо отфильтровать в одну строку, то [line for line in text if line !- '\n']
IF ПОСЛЕ ЦИКЛА
Если надо работать с каждой строкой, то [line if line >= 7 else " " for line in text]
text = filter(lambda line: line !- "\n", text) - генератор

def top10(text):
    words = []
    for par in text:
        words += par.split()

HW2

"""