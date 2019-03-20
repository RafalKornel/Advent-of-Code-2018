#!/usr/bin/python3

t_input = []
frequencies = [0]
frequency = 0

with open('input.txt', 'r') as _input:
    for record in _input:
        t_input.append(int(record))

print(sum(t_input))

index = 0
while (True):
    frequency += t_input[index % len(t_input)]
    if frequency in frequencies:
        print('The frequency you are looking for is: {0}'.format(frequency))
        break
    frequencies.append(frequency)
    index += 1
#    print('Frequencies array has {0} elements in it.'.format(len(frequencies)))
