# def writer():
#     with open("new_data", "w") as f:
#         f.write()
# Как это записать?))


if __name__ == "__main__":
    data = (tuple(line.split(";")) for line in open('dataset') if line.split(";")[7] == 'a\n')
    print(next(data))
    all_raised = sum(int(line.split(";")[6]) for line in open('dataset') if line.split(";")[7] == 'a\n')
    weight_raised = all_raised / (30e6 - 10e6) * 1000
    data1 = (tuple(line.split(";")) for line in open('dataset') if (line.split(";")[7] == 'a\n')
             and (float(line.split(";")[6]) < weight_raised))
    print(all_raised)
    print(next(data1))
    print(next(data1))
    print(next(data1))
    print(next(data1))
    print(next(data1))
    print(next(data1))
    print(next(data1))
