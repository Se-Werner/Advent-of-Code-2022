# Day 4; Part 1 of Advent of Code

with open('aoc_d04_input.txt') as file:
    lines = file.readlines()

clean_lines = []
for line in lines:
    clean_line = line.rstrip('\n')
    clean_line = clean_line.split(',')
    ready_line = []
    for pair in clean_line:
        elf = pair.split('-')
        ready_line.append(elf)

    clean_lines.append(ready_line)

solution_counter = 0
line_counter = 1
for group in clean_lines:
    index = 0
    for elf in group:
        if int(elf[0]) >= int(group[index-1][0]):
            if int(elf[1]) <= int(group[index-1][1]):
                solution_counter += 1
                # print(group)
                break
        index += 1

    # print(line_counter)
    line_counter += 1

print(f'The first solution is {solution_counter}\n')


# Solution for Part 2

solution_counter = 0
for group in clean_lines:
    if int(group[0][0]) >= int(group[1][0]) and int(group[0][0]) <= int(group[1][1]):
        solution_counter += 1
        # print(group)
    elif int(group[0][1]) >= int(group[1][0]) and int(group[0][1]) <= int(group[1][1]):
        solution_counter += 1
        # print(group)
    elif int(group[1][0]) >= int(group[0][0]) and int(group[1][0]) <= int(group[0][1]):
        solution_counter += 1
    elif int(group[1][1]) >= int(group[0][0]) and int(group[1][1]) <= int(group[0][1]):
        solution_counter += 1


print(f'The second Solution is {solution_counter}')
