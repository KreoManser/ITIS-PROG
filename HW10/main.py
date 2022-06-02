"""
    - 6 часов искал ошибку, а там надо было итерацию добавить, издевательская домашка :)
"""
from bs4 import BeautifulSoup
import re
import multiprocessing

with open('page.html') as fp:
    soup = BeautifulSoup(fp, 'lxml')

res = []
res0 = []

def one():
    for prod in soup.find_all('div', attrs='apartament'):
        title = prod.findChildren('h5', attrs='apartament-title')
        number = prod.findChildren('div', attrs='mobile-number')
        res0.append([title[0].text, number[0].text])


def file_reader(file):
    base = []
    with open(file) as f:
        for st in f:
            if 'Татарстан' in st:
                st = st.split(';')
                base.append([st[0], st[1], st[2]])
    # print(base)
    return base

def two():
    for i in res0:
        n = int(i[0].split(' ')[0][0])
        sqr = float(i[0].split(' ')[2])
        floor = int(re.findall(r'^\w+', i[0].split(' ')[4])[0])
        # for x in base:
        #     if (i[1][4:7] == x[0]) and (x[1] <= i[1][-7:] <= x[2]) and (45 <= sqr <= 65) and (
        #             3 <= floor <= 15) and n == 3:
        #         print("res append")
        #         res.append(i)
        for x in results:
            for b in x:
                if (i[1][4:7] == b[0]) and (b[1] <= i[1][-7:] <= b[2]) and (45 <= sqr <= 65) and (
                        3 <= floor <= 15) and n == 3:
                    # print("res append")
                    res.append(i)

def wrtiter():
    file = open('result.txt', 'w+')
    for i in res:
        # print("write")
        file.write(i[0] + ' ' + i[1] + '\n')
    file.close()


if __name__ == "__main__":
    one()
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(file_reader, ['8_ABC.csv', '4_ABC.csv', '3_ABC.csv', '9_ABC.csv'])
    two()
    wrtiter()
