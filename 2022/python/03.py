#!/usr/bin/env python3

'''
https://adventofcode.com/2022/day/3
'''
import string

IMPORTANCE_ORDER = string.ascii_lowercase + string.ascii_uppercase

with open('../inputs/03_input.txt', 'r', encoding='utf-8') as f:
    myinput = list(map(lambda x: x.strip(), f.readlines()))

repeated_item_per_rucksack = []
for rucksack in myinput:
    split = int(len(rucksack)/2)
    compartment_a = rucksack[:split]
    compartment_b = rucksack[split:]

    for item in compartment_a:
        if item in compartment_b:
            repeated_item_per_rucksack.append(
                IMPORTANCE_ORDER.index(item)+1
            )
            break

print(sum(repeated_item_per_rucksack))


## Part 2

badge_priority = []
team_rucksacks = []
for rucksack in myinput:
    team_rucksacks.append(list(rucksack))

    if len(team_rucksacks) == 3:
        for item in team_rucksacks[0]:
            if item in team_rucksacks[1] and item in team_rucksacks[2]:
                badge_priority.append(IMPORTANCE_ORDER.index(item) + 1)
                break

        team_rucksacks = []

print(sum(badge_priority))
