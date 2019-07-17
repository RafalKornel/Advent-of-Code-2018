#!/usr/bin/python3.7
from copy import deepcopy

class Star():
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, l = None):
        if not l:
            self.pos = {'x':_x, 'y':_y}
            self.vel = {'x':_vx, 'y':_vy}
        else:
            self.pos = {'x':l[0], 'y':l[1]}
            self.vel = {'x':l[2], 'y':l[3]}
    
    def move(self, dir = 1):
        self.pos['x'] += self.vel['x'] * dir
        self.pos['y'] += self.vel['y'] * dir

    def __str__(self):
        return f"x:{self.pos['x']} | y:{self.pos['y']} || v_x:{self.vel['x']} | v_y:{self.vel['y']}"

def calc_CM(stars):
    cm_x = 0
    cm_y = 0
    for star in stars:
        cm_x += star.pos['x']
        cm_y += star.pos['y']

    return {'x': cm_x / len(stars), 'y': cm_y / len(stars)}

def calc_dist_from_CM(stars, cm):
    d = 0
    for star in stars:
        d += ((star.pos['x'] - cm['x'])**2 + (star.pos['y'] - cm['y'])**2)**0.5

    return d / len(stars)

def evolve(stars):
    for star in stars:
        star.move()
    
def evolve_back(stars):
    for star in stars:
        star.move(-1)


stars = []

with open('input2.txt', 'r') as _input:
    for line in _input:
        #words = line.strip().split()
        words = line.replace('position=<', '') \
                    .replace('>', '') \
                    .replace('velocity=<', '') \
                    .replace('>', '') \
                    .replace(',', '') \
                    .split()
        stars.append(Star(l=list(map(int, words))))

min_dist = calc_dist_from_CM(stars, calc_CM(stars))
iter = 0

while(True): 
    cur_cm = calc_CM(stars)
    cur_dist = calc_dist_from_CM(stars, cur_cm)
    if cur_dist <= min_dist:
        min_dist = cur_dist
    else:
        break
    evolve(stars)
    iter += 1

evolve_back(stars)
#print(min_dist)
print(f"Number of years: {iter - 1}")

min_x = stars[0].pos['x']
min_y = stars[0].pos['y']
max_x = 0
max_y = 0
for star in stars:
    if star.pos['x'] < min_x: min_x = star.pos['x']
    if star.pos['y'] < min_y: min_y = star.pos['y']
    if star.pos['x'] > max_x: max_x = star.pos['x']
    if star.pos['y'] > max_y: max_y = star.pos['y']

print(min_x, min_y, '\t', max_x, max_y)

board = [ [False for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

for star in stars:
    #print(f"{star.pos['x'] - min_x} | {star.pos['y'] - min_y} ||| {max_x - min_x} | {max_y - min_y}")
    board[star.pos['y'] - min_y][star.pos['x'] - min_x] = True

with open("output.txt", 'w+') as out:
    for y in range(len(board)):
        s = ''
        for x in range(len(board[y])):
            if board[y][x]: s += '#'
            else: s += ' '
        s += '\n'
        out.write(s)




#print(calc_dist_from_CM(result, calc_CM(result)))