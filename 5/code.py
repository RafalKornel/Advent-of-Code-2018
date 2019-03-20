#!/usr/bin/python3

import re
_in = ''
alphabet = 'abcdefghijklmnopqrstuwvxyz'
with open('input.txt') as _input:
    _in += str(_input.read().strip())

def reduce_pol(_in):
    prev_len = 0
    while(True):
        prev_len = len(_in)
        for i in range(26):
            _in = _in.replace( (chr(ord('a') + i)) + (chr(ord('A') + i)) , '')
            _in = _in.replace( (chr(ord('A') + i)) + (chr(ord('a') + i)) , '')

        if len(_in) == prev_len:
            break

    return len(_in)

_inputs = [0] * 26
_lens = {}
for c in range(26):
    _inputs[c] = _in.replace(alphabet[c], '')
    _inputs[c] = _inputs[c].replace(alphabet[c].upper(), '')
    _lens[reduce_pol(_inputs[c])] = alphabet[c]

print(len(_in))
print(_lens)
print(min(_lens.keys()), _lens[min(_lens.keys())])
