from bs4 import BeautifulSoup
import re

with open('page.html') as fp:
    soup = BeautifulSoup(fp, 'lxml')
res = []
res0 = []
for prod in soup.find_all('div', attrs='apartament'):
    title = prod.findChildren('h5', attrs='apartament-title')
    number = prod.findChildren('div', attrs='mobile-number')
    res0.append([title[0].text, number[0].text])

base = []
with open('8_ABC.csv') as file:
    for st in file:
        if 'Татарстан' in st:
            st = st.split(';')
            base.append([st[0], st[1], st[2]])

with open('9_ABC.csv') as file:
    for st in file:
        if 'Татарстан' in st:
            st = st.split(';')
            base.append([st[0], st[1], st[2]])

for i in res0:
    n = int(i[0].split(' ')[0][0])
    sqr = float(i[0].split(' ')[2])
    floor = int(re.findall(r'^\w+', i[0].split(' ')[4])[0])
    for x in base:
        if (i[1][4:7] == x[0]) and (x[1] <= i[1][-7:] <= x[2]) and (45 <= sqr <= 65) and (3 <= floor <= 15) and n == 3:
            res.append(i)

file = open('result.txt', 'w+')
for i in res:
    file.write(i[0]+' '+i[1]+'\n')
file.close()
