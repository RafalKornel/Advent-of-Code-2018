#!/usr/bin/python3.7

import math

_input = 7400
size = 300
debug = True

grid =  [ [ 0 for _ in range(size)] \
               for _ in range(size) ] 

powers = [ [ [ 0 for _ in range(size - s - 1)]\
                 for _ in range(size - s - 1) ]\
                 for s in range(size) ]


def calc_power(x, y, _inp):
    rack_ID = x + 10
    power_level = rack_ID * y + _inp
    power_level *= rack_ID
    return int( ('00000' + str(power_level))[-3]) - 5

def test():
    print(calc_power(3, 5, 8))
    print(calc_power(122, 79, 57))
    print(calc_power(217, 196, 39))
    print(calc_power(101, 153, 71))

def biggest_div(n):
    dividors = []
    for i in range(1, math.ceil(n/2 + 1)):
        if n % i == 0:
            dividors.append(i)
    return max(dividors)
    

for y in range(size):
    for x in range(size):
        digit = calc_power(x, y, _input)
        grid[y][x] = digit

control = size

for s in range(1, control + 1):
    div = biggest_div(s)
    steps = int(s / div)

    if debug: print(f'size: {s}x{s} | div: {div} | steps: {steps}')
    for y in range(size - s):
        for x in range(size - s):
            #calculating total power for (x, y, size)
            cur_pow = 0
            for _y in range(steps):
                if s == 1: 
                    cur_pow += sum(grid[y + _y][x:x+s:div])
                else:      
                    cur_pow += sum(powers[div - 1][y + _y * div][x:x+s:div])
            powers[s - 1][y][x] = cur_pow

max_pow = {'x': 0, 'y': 0, 's': 0, 'pow': 0}

for s in range(1, control + 1):
    for y in range(size - s):
        for x in range(size - s):
            if powers[s - 1][y][x] > max_pow['pow']:
                max_pow['x'] = x
                max_pow['y'] = y
                max_pow['s'] = s
                max_pow['pow'] = powers[s - 1][y][x]
    if debug: print(max_pow)

print(max_pow)