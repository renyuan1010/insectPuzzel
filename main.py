from math import exp, log
from game import game
import copy
import random

game = game('input.txt')

iter = 100000  # number of iterations allowed
T = 1.0  # initial temperature
dec_cnt = 1 # decrease temperature every dec.cnt iterations
alpha = exp(log(1 / T) / (iter * 1.0 / dec_cnt))
d = 4
best = None
bestFit = 10000

for i in range(1, iter):
    if i % dec_cnt == 0:
        T = d / log(i + 1)   #1.0 / pow(i, log(2.5) / log(i + 1))
    newGame = copy.deepcopy(game)
    newGame.mutate()
    newfit = newGame.fitness()

    delta = newfit - game.fitness()

    if random.random() < exp(-delta / T):
        game = newGame

    if newfit < bestFit:
        bestFit = newfit
        best = newGame

    print('%s, %s, %s, %s' % (i, delta, T, game.fitness()))
    if game.fitness() == 0:
        break

print('done')
print(game.fitness())
print(best.fitness())
best.printout()