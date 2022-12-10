# Day 10, Part 1 of Advent of Code 2022 (we hit double digits)

with open('aoc_d10_input.txt') as file:
    input_lines = file.readlines()

input_clean = []
for line in input_lines:
    ready_line = line.rstrip('\n').split(' ')
    input_clean.append(ready_line)

x = 1
cycle_counter = 1
inst_counter = 0
command_counter = 0
target_counter = 20
solution_counter = 0

while cycle_counter <= 220:
    if cycle_counter == target_counter:
        signal_value = cycle_counter * x
        # print(x)
        solution_counter += signal_value
        target_counter += 40
    elif cycle_counter < target_counter:
        pass
    else:
        print('Error Target Count')

    if inst_counter == 0:
        if input_clean[command_counter][0] == 'noop':
            command_counter += 1
        elif input_clean[command_counter][0] == 'addx':
            inst_counter = 1
            command_value = int(input_clean[command_counter][1])
            # print(command_value)
            command_counter += 1
        else:
            print('Error Command Read')
    elif inst_counter == 1:
        inst_counter = 0
        x += command_value
    else:
        print('Error Instruction Count')

    if cycle_counter == target_counter:
        signal_value = cycle_counter * x
        print(x)
        solution_counter += signal_value
        target_counter += 40
    elif cycle_counter < target_counter:
        pass
    else:
        print('Error Target Count')
    # print(x)
    cycle_counter += 1

print(f'The first Solution is {solution_counter}\n')


# Solution for Part 2

x = 1
cycle_counter = 1
sub_cycle_counter = 0
inst_counter = 0
command_counter = 0
target_counter = 40
list_solution = []
render_line = ''

while cycle_counter <= 240:
    if abs(x - sub_cycle_counter) <= 1:
        render_line += '#'
    elif abs(x - sub_cycle_counter) > 1:
        render_line += '.'
    else:
        print('Error Render')

    if cycle_counter == target_counter:
        list_solution.append(render_line)
        render_line = ''
        target_counter += 40
        sub_cycle_counter = 0
    elif cycle_counter < target_counter:
        sub_cycle_counter += 1
    else:
        print('Error Target Counter 2')

    if inst_counter == 0:
        if input_clean[command_counter][0] == 'noop':
            command_counter += 1
        elif input_clean[command_counter][0] == 'addx':
            inst_counter = 1
            command_value = int(input_clean[command_counter][1])
            # print(command_value)
            command_counter += 1
        else:
            print('Error Command Read 2')
    elif inst_counter == 1:
        inst_counter = 0
        x += command_value
    else:
        print('Error Instruction Count 2')

    cycle_counter += 1

for x in list_solution:
    print(x)