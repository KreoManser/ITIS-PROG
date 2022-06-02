import pickle


def func1(arr):
    filtered = []
    for element in arr:
        for elem in element.split():
            if elem.isalpha():
                filtered.append(elem)
            else:
                new_elem = list(filter(str.isalpha, elem))
                str_elem = ''
                for elem_ in new_elem:
                    str_elem += elem_
                filtered.append(str_elem)
    overMore = [word for word in filtered if len(word) > 5]
    array = {}.fromkeys(overMore, 0)
    for word in overMore:
        array[word] += 1
    sorted_array = sorted(array.items(), key=lambda thud: thud[1])
    top10 = sorted_array[-1:-11:-1]
    return top10


def func2(arr):
    len_ = list(map(len, arr))
    return sum(len_) / len(len_)


def func3(data_array):
    author = []
    text = []
    for i in range(len(data_array)):
        if not data_array[i].get('edited'):
            if data_array[i].get('author') != '[deleted]':
                author.append([data_array[i].get('score'), data_array[i].get('author')])
                text.append([data_array[i].get('score'), data_array[i].get('body')])
    author.sort(reverse=True)
    author_ = [i[1] for i in author[0:10]]
    text.sort(reverse=True)
    text_ = [i[1] for i in text[0:10]]
    return author_, text_


def func4(data_array):
    score = []
    for i in range(len(data_array)):
        score.append([data_array[i].get('score'), data_array[i].get('body')])
    score.sort()
    score_ = [i[1] for i in score[0:10]]
    return score_


def func5(arr, word):
    counter = 0
    for elem in arr:
        for elem_ in elem.split():
            if word.lower() in elem_.lower():
                counter += 1
    return counter / len(arr)


if __name__ == "__main__":
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
        body = [data[i].get('body') for i in range(len(data))]
    # print(func1(body))
    # print(func2(body))
    # print(func3(data))
    # print(func4(data))
    # print(func5(body, "kwh"))
