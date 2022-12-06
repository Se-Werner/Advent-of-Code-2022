# Day 6, Part 1 of Advent of Code

with open('aoc_d06_input.txt') as file:
    input_stream = file.read()

char_counter = 0
buffer_lng = []
for x in input_stream:
    char_counter += 1
    if len(buffer_lng) <= 2:
        buffer_lng.append(x)
    elif len(buffer_lng) == 3:
        buffer_lng.append(x)
        buffer_tmp = []
        double_counter = 0
        for y in buffer_lng:
            if y in buffer_tmp:
                double_counter += 1
            buffer_tmp.append(y)
        if double_counter == 0:
            break
        elif double_counter > 0:
            pass
        else:
            print('Error: Double Counter')
        del buffer_lng[0]
    else:
        print('Error: Buffer Length')

print(f'The first Solution is: {char_counter}\n')

# Solution for Part 2

char_counter = 0
buffer_lng = []
for x in input_stream:
    char_counter += 1
    if len(buffer_lng) <= 12:
        buffer_lng.append(x)
    elif len(buffer_lng) == 13:
        buffer_lng.append(x)
        buffer_tmp = []
        double_counter = 0
        for y in buffer_lng:
            if y in buffer_tmp:
                double_counter += 1
            buffer_tmp.append(y)
        if double_counter == 0:
            break
        elif double_counter > 0:
            pass
        else:
            print('Error: Double Counter')
        del buffer_lng[0]
    else:
        print('Error: Buffer Length')

print(f'The first Solution is: {char_counter}\n')
