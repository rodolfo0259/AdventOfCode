#!/usr/bin/env python3
'''
https://adventofcode.com/2022/day/1
'''

# part one

with open('../inputs/01_input.txt', 'r', encoding='utf-8') as f:
    myinput = list(map(lambda x: x.strip(), f.readlines()))

elves_inventory = ([
        list(map(int, item.split('@')))
        for item in '@'.join(myinput).split('@@')
    ]
)

total_snacks_by_elf = sorted(list(map(sum, elves_inventory)))

print(total_snacks_by_elf[-1])

# part two

print(sum(total_snacks_by_elf[-3:]))
