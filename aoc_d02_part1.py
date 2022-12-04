# Day 2, part 1 of Advent of Code 2022

with open('aoc_d02_input.txt') as file:
    lines = file.readlines()

content = []
for line in lines:
    line = line.rstrip('\n')
    content.append(line)

cases_1 = {'A Y': 8, 'A X': 4, 'A Z': 3,
           'B Y': 5, 'B X': 1, 'B Z': 9,
           'C Y': 2, 'C X': 7, 'C Z': 6}

solution_counter = 0
for c_round in content:
    solution_counter += cases_1[c_round]

print(f'The Solution is {solution_counter} Points')


# Part 2 Solution

cases_2 = {'A X': 3, 'A Y': 4, 'A Z': 8,
           'B X': 1, 'B Y': 5, 'B Z': 9,
           'C X': 2, 'C Y': 6, 'C Z': 7}

solution_counter = 0
for c_round in content:
    solution_counter += cases_2[c_round]

print(f'\nThe second Solution is {solution_counter} points')
