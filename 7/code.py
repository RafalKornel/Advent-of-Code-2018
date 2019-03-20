#!/usr/bin/python3

_in = []
workers_count = 15

steps_outputs = {}
steps_inputs = {}

path = ''
nodes = ''

with open('input.txt', 'r') as _input:
    for line in _input:
        current = [line.split()[1], line.split()[7]]
        _in.append( current )
        for i in range(2):
            if current[i] not in nodes:
                nodes += current[i]

def return_node_with_empty_input():
    for node in ''.join(sorted(nodes)):
        if steps_inputs[node] == '' and node not in working_on:
            return node
    return ''

def remove_node_from_inputs(node):
    for step in steps_inputs:
        if node in steps_inputs[step]:
            steps_inputs[step] = steps_inputs[step].replace(node, '')

def check_if_workers_are_done(workers):
    _sum = 0
    for worker in workers:
        _sum += worker[0]

    return True if _sum == 0 else False

for step in _in:
    try: steps_outputs[step[0]] += step[1]
    except: steps_outputs[step[0]] = step[1]

for step in _in:
  try: steps_inputs[step[1]] += step[0]
  except: steps_inputs[step[1]] = step[0]

for n in nodes:
    if n not in steps_inputs:
        steps_inputs[n] = ''

_current = ''
workers = [ [0, ''] ] * workers_count
overall_time = 0
working_on = ''

timer = 0

while True:
    for i in range(len(workers)):
        if workers[i][0] == 0:
            path += workers[i][1]
            nodes = nodes.replace(workers[i][1], '')
            remove_node_from_inputs(workers[i][1])
            workers[i][1] = ''
            _current = return_node_with_empty_input()
            if _current not in working_on:
                try: workers[i] = [ord(_current) - 65 + 60, _current]
                except: pass
                finally: working_on += _current

        else:
            workers[i][0] -= 1

    if len(nodes) == 0: break

    overall_time += 1

print(path)
print(overall_time)

#        print('Current worker: {0} | workers: {1} | nodes: {2} | nodes\' inputs: {3} | current var: {4} | path: {5} | time: {6}'.format(i, workers[i], nodes, steps_inputs, _current, path, overall_time))
