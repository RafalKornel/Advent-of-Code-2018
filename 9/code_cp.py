#!/usr/bin/python3.7


class Marble():

    def __init__(self, number):
        self.number = number
        self.is_current = False


    def set_current(self, current):
        self.is_current = current


class Circle():

    def __init__(self, players_count):
        self.marbles = [ Marble(0) ]
        self.current_marble = self.marbles[0]
        self.players_scores = [0] * players_count


    def add_marble(self, marble, player):
        current_marble_index = self.marbles.index(self.current_marble)

        if marble.number % 23 != 0:
            self.marbles.insert((current_marble_index + 2) % len(self.marbles), marble)
            self.current_marble = marble

        else:
            self.players_scores[player] += marble.number
            self.players_scores[player] += self.marbles[current_marble_index - 7].number
            self.current_marble = self.marbles[current_marble_index - 6]
            self.marbles.pop(current_marble_index - 7)


    def __str__(self):
        result = []
        for marble in self.marbles:
            result.append(marble.number)
        return str(result)


player_count = 432
last_marble = 7101900
circle = Circle(player_count)
cur_marble = 1

while(cur_marble < last_marble):

    for pl in range(player_count):
        circle.add_marble(Marble(cur_marble), pl)
        cur_marble += 1

#print(circle)
#print(circle.players_scores)
print(max(circle.players_scores))
