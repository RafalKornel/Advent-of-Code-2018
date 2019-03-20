#!/usr/bin/python3

from datetime import datetime

t_input = []
temp = []
guards = {}
table = []
with open('input.txt', 'r') as _input:
    for record in _input:
        temp.append(record)

temp.sort()
current_guard = 0
temp_datetime = datetime.now()

for record in temp:
    _datetime = datetime.strptime(record[1:record.index(']'):], '%Y-%m-%d %H:%M')
    _log = record[record.index(']') + 1:].strip('\n')

    try:
        _log.index('#')
        current_guard = int(_log.split()[1][1::])
    except: pass

    if _log == ' falls asleep': temp_datetime = _datetime
    if _log == ' wakes up':
        diff = (_datetime - temp_datetime).total_seconds()
        if (current_guard) in guards: guards[current_guard] += diff
        else: guards[current_guard] = diff


    t_input.append( [_datetime, _log, current_guard] )

table = { guard: { minute:0 for minute in range(0, 60)} for guard in guards }

temp_time = datetime.now()
for record in t_input:
    if record[1] == ' falls asleep': temp_time = record[0]
    if record[1] == ' wakes up':
        diff = int((record[0] - temp_time).total_seconds()/60)
        for m in range(diff):
            table[record[2]][m + temp_time.minute] += 1

most_aslept = []
for guard in table:
    most_aslept.append( [guard, max(table[guard].values())] )


print(most_aslept)
print(table[1997])
#print(table[2351], max(table[2351].values()))
#print(guards)
#guard = int(max(guards.values())/60)
#print(guard * 60)
#print(guard, table[guard])
