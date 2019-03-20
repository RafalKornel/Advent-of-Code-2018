#!/usr/bin/python3.5
from blist import blist

class Circle():

    def __init__(self, players_count):
        self.marbles = blist([ 0 ])
        self.current_marble = self.marbles[0]
        self.players_scores = [0] * players_count


    def add_marble(self, marble, player):
        current_marble_index = self.marbles.index(self.current_marble)

        if marble % 23 != 0:
            self.marbles.insert((current_marble_index + 2) % len(self.marbles), marble)
            self.current_marble = marble

        else:
            self.players_scores[player] += marble + self.marbles[current_marble_index - 7]
            self.current_marble = self.marbles[current_marble_index - 6]
            self.marbles.pop(current_marble_index - 7)


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
    print(cur_marble)
print(max(circle.players_scores))
