#!/usr/bin/env python3
'''
https://adventofcode.com/2022/day/2
'''

## Extra Chanllenge: don't use for..loop
# part one

with open('../inputs/02_input.txt', 'r', encoding='utf-8') as f:
    myinput = list(map(lambda x: x.strip().split(' '), f.readlines()))

print(myinput)

values = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

translation = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

win = {
    'X': 'Z',  # Rock
    'Y': 'X',  # Paper
    'Z': 'Y',  # Scissors
}
match_values = list(map(
    lambda x: values[x[1]] + (
        3 if translation[x[0]] == x[1] else (
            0 if win[translation[x[0]]] == x[1] else 6
        )
    ), myinput
))

print(sum(match_values))

# part two

strategy = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def strategy_plan(x):
    final_value = strategy[x[1]]
    oponent = translation[x[0]]
    lose = win[oponent]
    if x[1] == 'X':
        final_value += values[lose]
    elif x[1] == 'Y':
        final_value += values[oponent]
    else:
        vals = ['X', 'Y', 'Z']
        vals.remove(oponent)
        vals.remove(lose)
        final_value += values[vals[0]]

    return final_value


lose_draw_win = list(map(strategy_plan, myinput))
print(sum(lose_draw_win))

# I created a little monster
