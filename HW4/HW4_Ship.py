import random


def field():
    field_ = [["~" for j in range(7)] for i in range(7)]
    return field_


def ships(field__):
    for i in range(11):
        x_c = random.randint(0, 6)
        y_c = random.randint(0, 6)
        if field__[x_c][y_c] == "*":
            i -= 1
        else:
            field__[x_c][y_c] = "*"
    return field__


def print_field(field___):
    print("\n".join(" ".join(i) for i in field___))


def attack(back_field, front_field):
    kill_count = 0
    coord = input(f'Введите координаты ')
    while True:
        if (coord == "quit") or (kill_count == 10):
            break
        else:
            index = coord.split()
            x = int(index[0])
            y = int(index[1])
            # print(index)
            if back_field[x][y] == "*":
                front_field[x][y] = "X"
                print("RIP")
                print_field(front_field)
                # print("\n")
                # print(print_field(back_field))
                kill_count += 1
            elif front_field[x][y] == "o" or front_field[x][y] == "X":
                print("Эта клетка уже открыта")
                print_field(front_field)
                # print("\n")
                # print(print_field(back_field))
            else:
                front_field[x][y] = "o"
                print("MISS")
                print_field(front_field)
                # print("\n")
                # print(print_field(back_field))
        coord = input(f'Введите координаты ')


if __name__ == "__main__":
    back_field_ = field()
    front_field_ = field()
    ship_put = ships(back_field_)
    attack_ships = attack(back_field_, front_field_)