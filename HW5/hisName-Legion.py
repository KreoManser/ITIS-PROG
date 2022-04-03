import random

class Warrior:
    def __init__(self, name="No name", race="не указано", gender="не указано", evasion_prob=0, buff_scale=1):
        self.name = name
        self.max_hp = 100
        self.hp = 100
        self.race = race
        self.gender = gender
        self.evasion_prob = evasion_prob
        self.buff_scale = buff_scale

    def attack(self, enemy, damage=0):
        if random.random() < 1 - enemy.evasion_prob:
            enemy.hp -= damage * self.buff_scale

    def __repr__(self):
        return f'I am {self.race, self.gender}, my name is {self.name}, {self.hp} heal points'


class Human(Warrior):
    def __init__(self, race="Человек", buff_scale=1.1):
        super().__init__(self.max_hp, self.hp, self.evasion_prob)
        self.race = race
        self.buff_scale = buff_scale


class Light(Human):
    def __init__(self, name="No", gender="No", evasion_prob=0.3):
        super(Human).__init__(self.race, self.buff_scale)
        self.name = name
        self.gender = gender
        self.max_hp = 200
        self.hp = 200
        self.evasion_prob = evasion_prob

    def attack(self, enemy, damage=0):
        damage = random.randrange(30, 51)
        if random.random() < 1 - enemy.evasion_prob:
            enemy.hp -= damage * self.buff_scale


class Heavy(Human):
    def __init__(self, name="No", gender="No", evasion_prob=0):
        super(Human).__init__(self.race, self.buff_scale)
        self.name = name
        self.gender = gender
        self.max_hp = 500
        self.hp = 500
        self.evasion_prob = evasion_prob

    def attack(self, enemy, damage=0):
        damage = random.randrange(50, 71)
        if random.random() < 1 - enemy.evasion_prob:
            enemy.hp -= damage * self.buff_scale


class Druid(Human):
    def __init__(self, name="No", gender="No", evasion_prob=0.7):
        super(Human).__init__(self.race, self.buff_scale)
        self.name = name
        self.gender = gender
        self.max_hp = 100
        self.hp = 100
        self.evasion_prob = evasion_prob

    def attack(self, enemy, damage=0):
        if random.random() <= 0.3 and enemy != Shaman:
            enemy.hp = 10

    def heal(self, enemy):
        if random.random() > self.evasion_prob and enemy != Druid:
            enemy.hp = enemy.max_hp


class Ork(Warrior):
    def __init__(self, race="Орк", buff_scale=1.1):
        super().__init__(self.max_hp, self.hp, self.evasion_prob)
        self.race = race
        self.buff_scale = buff_scale


class Berserker(Ork):
    def __init__(self, name="No", gender="No", evasion_prob=0.1):
        super(Ork).__init__(self.race, self.buff_scale)
        self.name = name
        self.gender = gender
        self.max_hp = 600
        self.hp = 600
        self.evasion_prob = evasion_prob

    def attack(self, enemy, damage=0):
        damage = random.randrange(60, 91)
        if random.random() < 1 - enemy.evasion_prob:
            enemy.hp -= damage * self.buff_scale


class Shaman(Ork):
    def __init__(self, name="No", gender="No", evasion_prob=0.7):
        super(Ork).__init__(self.race, self.buff_scale)
        self.name = name
        self.gender = gender
        self.max_hp = 120
        self.hp = 120
        self.evasion_prob = evasion_prob

    def attack(self, enemy, damage=0):
        if random.random() <= 0.5 and enemy != Druid:
            enemy.hp = 10

    def heal(self, enemy):
        if random.random() > self.evasion_prob and enemy != Shaman:
            enemy.hp = enemy.max_hp


def add_pull():
    list_of_value = [12, 11, 15, 8, 7]
    lights = []  # Light, Heavy, Druid
    darks = []  # berserker, shaman

    for char in range(list_of_value[0]):
        lights.append(Light())
    for char in range(list_of_value[1]):
        lights.append(Heavy())
    for char in range(list_of_value[2]):
        lights.append(Druid())

    for char in range(list_of_value[3]):
        darks.append(Berserker())
    for char in range(list_of_value[4]):
        darks.append(Shaman())
    return [lights, darks]


def fights(pole):
    hp_human_race = 0
    hp_magic_race = 0

    for enemy in pole[0]:
        hp_human_race += enemy.hp

    for enemy in pole[1]:
        hp_magic_race += enemy.hp


# if __name__ == "__main__":
