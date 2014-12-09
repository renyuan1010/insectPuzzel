from piece import piece
import random
from math import sqrt


class game(object):
    def __init__(self, file):
        self.board = [[piece(None) for x in range(3)] for x in range(3)]

        f = open(file, 'r')

        list = []
        for i in range(9):
            data = [[0 for x in range(3)] for x in range(3)]
            for j in range(3):
                line = f.readline().split(',')
                for k in range(3):
                    data[j][k] = int(line[k])
            list.append(piece(data))

        for i in range(3):
            for j in range(3):
                self.board[i][j] = list[i * 3 + j]

        f.close()

    def exchange(self):
        # randomly pick two pieces and exchange their positions
        ind = range(9)
        p1 = ind[random.randint(0, 8)]
        ind.remove(p1)
        p2 = ind[random.randint(0, 7)]

        tmp = self.board[p1 / 3][(p1 - 1) % 3]
        self.board[p1 / 3][(p1 - 1) % 3] = self.board[p2/3][(p2-1) % 3]
        self.board[p2/3][(p2-1) % 3] = tmp

    def rotate(self):
        ind = range(9)[random.randint(0, 8)]
        self.board[ind / 3][(ind - 1) % 3].rotate()

    def add(self, p1, p2, vertical):
        if vertical:
            return int(p1.data[2][1] + p2.data[0][1] != 0)
        else:
            return int(p1.data[1][2] + p2.data[1][0] != 0)

    def fitness(self):
        fit = self.add(self.board[0][0], self.board[0][1], False) \
            + self.add(self.board[0][1], self.board[0][2], False) \
            + self.add(self.board[1][0], self.board[1][1], False) \
            + self.add(self.board[1][1], self.board[1][2], False) \
            + self.add(self.board[2][0], self.board[2][1], False) \
            + self.add(self.board[2][1], self.board[2][2], False) \
            + self.add(self.board[0][0], self.board[1][0], True) \
            + self.add(self.board[1][0], self.board[2][0], True) \
            + self.add(self.board[0][1], self.board[1][1], True) \
            + self.add(self.board[1][1], self.board[2][1], True) \
            + self.add(self.board[0][2], self.board[1][2], True) \
            + self.add(self.board[1][2], self.board[2][2], True)

        return fit

    def mutate(self):
        rand = random.random()
        if rand < 0.5:
            self.exchange()
        else:
            self.rotate()

    def printout(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j].data)
