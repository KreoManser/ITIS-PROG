import random


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def hit(self):
        return random.random() < 0.8

    def score(self):
        return int(self.score)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start(self):
        count = 0
        score_p1 = 0
        score_p2 = 0
        while (score_p1 != 11) or (score_p2 != 11):
            count += 1
            if count % 2 == 1:
                while p1.hit():
                    p2.hit()
                score_p2 += 1
            if count % 2 == 0:
                while p2.hit():
                    p1.hit()
                score_p1 += 1


if __name__ == "__main__":
    p1 = Player('Ping')
    p2 = Player('Pong')
    game = Game(p1, p2)
    print(game.start())
