import random
import copy

class piece(object):

    def __init__(self, data):
        self.data = data

    def rotate(self):
        rotated = copy.deepcopy(self.data)

        if random.random() < 0.5:  # rotate clockwise
            for i in range(3):
                for j in range(3):
                    rotated[i][j] = self.data[2 - j][i]
        else:
            for i in range(3):
                for j in range(3):
                    rotated[i][j] = self.data[j][2 - i]

        self.data = rotated

