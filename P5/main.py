if __name__ == "__main__":
    # l1 = [[1, 2, 3], [2], [4, 5, 6], [0]]
    # # [1, 2, 3, 2, 4, 5, 6, 0]
    # l2 = [element for sub_list in l1 for element in sub_list]
    # print(l2)
    a = [1, 1, 2, 2, 3]
    b = [2, 1, 1, 1, 3, 2]
    res = [value for value in a if value in b]
    print(res)
    