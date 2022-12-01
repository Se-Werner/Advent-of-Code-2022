# Day 1, Part 1 of the 2022 Advent of Code

with open('aoc_d01_input.txt') as file:
    lines = file.readlines()

clean_lines = []
for line in lines:
    clean_line = line.rstrip('\n')
    clean_lines.append(clean_line)

elves = []
calories = 0
for line in clean_lines:
    if line == '':
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)

high_score = 0
for elf in elves:
    if elf > high_score:
        high_score = elf
    elif elf <= high_score:
        pass
    else:
        print(f'Error High Score : {elf}')

print(f'The solution is {high_score} calories.')

# solution for part 2

p2_high_scores = []

for elf in elves:
    if len(p2_high_scores) < 3:
        p2_high_scores.append(elf)
        p2_high_scores.sort()
    elif len(p2_high_scores) == 3:
        if elf > p2_high_scores[0]:
            del p2_high_scores[0]
            p2_high_scores.append(elf)
            p2_high_scores.sort()
        elif elf <= p2_high_scores[0]:
            pass
        else:
            print(f'Error P2 High-Score: {elf}')
    else:
        print(f'Error Check List Length: {len(p2_high_scores)}')

solution_counter = 0
for big_elf in p2_high_scores:
    solution_counter += big_elf

print(f'\nThe Solution to part 2 is {solution_counter} calories')
