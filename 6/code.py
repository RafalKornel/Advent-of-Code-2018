#!/usr/bin/python3

x_bound = 0
y_bound = 0

with open('input.txt', 'r') as _input:
    points = [list(map(int, line.strip().replace(' ', '').split(','))) for line in _input]

x_bound = max([int(coord[0]) for coord in points])
y_bound = max([int(coord[1]) for coord in points])

points_counts= {i:0 for i in range(len(points))}
plane = [ [0] * x_bound for i in range(y_bound) ]

def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def first_part():
    for y in range(y_bound):
        for x in range(x_bound):
            lengths = [ calculate_distance([x, y], point) for point in points]
            if plane[y][x] == 0:
                _min = min(lengths)
                i = lengths.index(_min)
                if lengths.count(_min) == 1:
                    plane[y][x] = i
                    points_counts[i] += 1
                else:
                    plane[y][x] = -1

    edges = [ plane[y][x] for x in [0, x_bound - 1] for y in [0, y_bound - 1] ]

    control = True
    while control:
        _max = max(points_counts.values())
        for point in points_counts:
            if points_counts[point] == _max and point not in edges:
                print(points_counts[point])
                control = False
            elif point in edges:
                points_counts[point] = 0


def second_part():
    region_size = 0
    for y in range(y_bound):
        for x in range(x_bound):
            lengths = [ calculate_distance([x, y], point) for point in points]
            if sum(lengths) < 10000:
                region_size += 1
    print(region_size)

second_part()
#print(points_counts)
#print(points)
#print(plane)
