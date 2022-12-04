# Day 3, Part 1 of Advent of Code
import string

with open('aoc_d03_input.txt') as file:
    rucksack_content = file.readlines()

prio_counter = 1
prio_key = {}
for char in string.ascii_lowercase:
    prio_key[char] = prio_counter
    prio_counter += 1

for char in string.ascii_uppercase:
    prio_key[char] = prio_counter
    prio_counter += 1


solution_counter = 0
line_counter = 1
for sack in rucksack_content:
    split_point = int(len(sack) / 2)
    for i in range(0, split_point):
        if sack[i] in sack[split_point: ]:
            solution_counter += prio_key[sack[i]]
            line_points = prio_key[sack[i]]  # Debug Line
            # print(f'Debug Char: {sack[i]} with point {prio_key[sack[i]]}')
            break

    # print(f'Debug: Line {line_counter}: {line_points}')
    line_counter += 1  # Debug Line
    line_points = 0  # Debug Line

print(f'The first Solution is {solution_counter}\n')


# Part 2 Solution

groups = []
elves = []
for elf in rucksack_content:
    if len(elves) < 2:
        elves.append(elf)
    elif len(elves) == 2:
        elves.append(elf)
        groups.append(elves)
        elves = []
    else:
        print(f'Error Group Selection: {elves}')

solution_counter = 0
for group in groups:
    for item in group[0]:
        if item in group[1]:
            if item in group[2]:
                solution_counter += prio_key[item]
                break

print(f'The second Solution is {solution_counter}')