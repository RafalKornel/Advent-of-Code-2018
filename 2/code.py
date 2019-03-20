#!/usr/bin/python3

twos = 0
threes = 0
t_input = []
with open('input.txt', 'r') as _input:
    for line in _input:
        t_input.append(line.strip())
        d = dict()
        for letter in line:
            try: d[letter] += 1
            except KeyError: d[letter] = 1
        twos += 1 if 2 in list(d.values()) else 0
        threes += 1 if 3 in list(d.values()) else 0

for _line in t_input:
    for line in t_input:
        dupa = 0
        index_dupa = 0
        for i in range(len(_line)):
            if _line[i] != line[i]:
                dupa += 1
                index_dupa = i
        if dupa == 1:
            #print(_line, line)
            print(list(_line), (_line[index_dupa]), _line[:index_dupa] + _line[index_dupa + 1:])


print(twos * threes)
#print(t_input)
