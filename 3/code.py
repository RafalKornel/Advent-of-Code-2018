#!/usr/bin/python3

import re

t_input = []

with open('input.txt', 'r') as _input:
    for line in _input:
        t_input.append(list(map(lambda _str : int(_str), re.split('[#@,:x]', line[1::].strip()))))

fabric = [ [[] for x in range(1000)] for y in range(1000)]
#fabric = [ [0 for x in range(10)] for y in range(10)]

def claim_space(record):
    id = record[0]
    x, y = record[1], record[2]
    width, height = record[3], record[4]

    for _y in range(height):
        for _x in range(width):
            fabric[y + _y][x + _x].append(id)

for record in t_input:
    claim_space(record)

count = 0


for y in fabric:
    for x in y:
        if len(x) > 1:
            count += 1
            for _id in x:
                t_input[_id - 1].append(1)

for r in t_input:
    if len(r) == 5:
        print (r[0])

#for s in fabric:
#    print(s)
print(count)
