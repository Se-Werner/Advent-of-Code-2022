# Day 5, Part 1 of Advent of Code
import copy

# Setting up the model for the crates
with open('aoc_d05_input_a.txt') as file:
    input_a_raw = file.readlines()

crate_grid = {}
for x in range(-1, -1 - len(input_a_raw), -1):
    if x == -1:
        for y in range(1, len(input_a_raw[x]), 4):
            crate_grid[input_a_raw[x][y]] = []
    elif x <= -1:
        for y in range(1, len(input_a_raw[x]), 4):
            if input_a_raw[x][y] != ' ':
                crate_grid[input_a_raw[-1][y]].append(input_a_raw[x][y])
    else:
        print('Error Set Up crate_grid')

crate_grid_2 = copy.deepcopy(crate_grid)  # create a copy for part 2


# Preparing the read in of the commands
with open('aoc_d05_input_b.txt') as file_b:
    input_b_raw = file_b.readlines()

key_counter = 1
dict_cmd = {}
for line_b in input_b_raw:
    line_b = line_b.rstrip('\n')
    line_b = line_b.split(' ')
    dict_cmd[str(key_counter)] = {'nmb': line_b[1], 'src': line_b[3], 'dst': line_b[5]}
    key_counter += 1


# executing commands

for cmd_key in dict_cmd.keys():
    cmd_counter = 1
    while cmd_counter <= int(dict_cmd[cmd_key]['nmb']):
        crate_grid[dict_cmd[cmd_key]['dst']].append(crate_grid[dict_cmd[cmd_key]['src']][-1])
        del crate_grid[dict_cmd[cmd_key]['src']][-1]
        cmd_counter += 1

solution = ''
for z in crate_grid.keys():
    solution += crate_grid[z][-1]

print(f'The solution code is: {solution}\n')


# solution for part 2
for cmd_key in dict_cmd.keys():
    buffer = []
    cmd_counter = 1
    while cmd_counter <= int(dict_cmd[cmd_key]['nmb']):
        buffer.append(crate_grid_2[dict_cmd[cmd_key]['src']][-1])
        del crate_grid_2[dict_cmd[cmd_key]['src']][-1]
        cmd_counter += 1

    while len(buffer) > 0:
        crate_grid_2[dict_cmd[cmd_key]['dst']].append(buffer[-1])
        del buffer[-1]

solution = ''
for z in crate_grid_2.keys():
    solution += crate_grid_2[z][-1]

print(f'The second solution code is: {solution}')
