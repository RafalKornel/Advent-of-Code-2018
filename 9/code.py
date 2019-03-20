#!/usr/bin/python3.5
from blist import blist
from collections import deque


class Circle():

    def __init__(self, players_count):
        self.marbles = deque([0])
        self.players_scores = [0] * players_count


    def add_marble(self, marble, player):
        if marble % 23 != 0:
            self.marbles.rotate(-2)
            self.marbles.appendleft(marble)

        else:
            self.marbles.rotate(7)
            self.players_scores[player] += marble + self.marbles.popleft()


    def __str__(self):
        result = []
        for marble in self.marbles:
            result.append(marble)
        return str(result)


player_count = 432
last_marble = 7101900
circle = Circle(player_count)
cur_marble = 1

while(cur_marble < last_marble):

    for pl in range(player_count):
        circle.add_marble(cur_marble, pl)
        cur_marble += 1
print(max(circle.players_scores))
