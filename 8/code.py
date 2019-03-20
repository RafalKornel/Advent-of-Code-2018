#!/usr/bin/python3

_input = ''
_sum = 0
nodes = []
_index = 0

class Node():
    def __init__(self, _input):
        global _index
        self.child_count = int(_input.pop())
        self.metadata_count = int(_input.pop())
        self.children = []
        self.data = []
        self.value = 0
        self.index = _index
        _index += 1

        for i in range(self.child_count):
            self.children.append(Node(_input))

        for i in range(self.metadata_count):
            self.data.append(int(_input.pop()))

        nodes.append(self)
        self.sum = sum(self.data)

        if self.child_count != 0:
            for _data in self.data:
                try:
                    self.value += self.children[_data - 1].value
                except:
                    pass

        else:
            for _data in self.data:
                self.value += _data

    def __str__(self):
        return 'The {3} node has {0} subnodes and {1} metadata entries: {2}'.format(self.child_count, self.metadata_count, self.data, self.index)

with open('input.txt', 'r') as _in:
    for line in _in:
        _input += line
    _input = _input.split()
    _input = _input[::-1]

node = Node(_input)
print(node)
print('Root node value is: {0}'.format(node.value))
