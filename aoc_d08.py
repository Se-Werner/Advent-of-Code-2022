# Day 8, Part 1 of Advent of Code 2022


with open('aoc_d08_input.txt') as file:
    input_lines = file.readlines()

ready_lines = []
for x in input_lines:
    line = x.rstrip('\n')
    ready_lines.append(line)

y_dim = len(ready_lines)
x_dim = len(ready_lines[0])

dict_grid = {}
line_counter = 1
for line in ready_lines:
    dict_line = {}
    row_counter = 1
    for y in line:
        dict_tree = {'height': int(y), 'visible': True}
        dict_line[row_counter] = dict_tree
        row_counter += 1

    dict_grid[line_counter] = dict_line
    line_counter += 1

for y_key in dict_grid.keys():
    for x_key in dict_grid[y_key].keys():
        visible_counter = 0
        if x_key == 1 or y_key == 1:
            pass
        elif x_key == x_dim or y_key == y_dim:
            pass
        else:
            for y in range(1, y_key):
                if dict_grid[y][x_key]['height'] >= dict_grid[y_key][x_key]['height']:
                    visible_counter += 1
                    break
                elif dict_grid[y][x_key]['height'] < dict_grid[y_key][x_key]['height']:
                    pass

            for y in range(y_key + 1, y_dim + 1):
                if dict_grid[y][x_key]['height'] >= dict_grid[y_key][x_key]['height']:
                    visible_counter += 1
                    break
                elif dict_grid[y][x_key]['height'] < dict_grid[y_key][x_key]['height']:
                    pass

            for x in range(1, x_key):
                if dict_grid[y_key][x]['height'] >= dict_grid[y_key][x_key]['height']:
                    visible_counter += 1
                    break
                elif dict_grid[y_key][x]['height'] < dict_grid[y_key][x_key]['height']:
                    pass

            for x in range(x_key + 1, x_dim + 1):
                if dict_grid[y_key][x]['height'] >= dict_grid[y_key][x_key]['height']:
                    visible_counter += 1
                    break
                elif dict_grid[y_key][x]['height'] < dict_grid[y_key][x_key]['height']:
                    pass

            if visible_counter == 4:
                dict_grid[y_key][x_key]['visible'] = False

solution_counter = 0
for y_key in dict_grid.keys():
    for x_key in dict_grid[y_key]:
        if dict_grid[y_key][x_key]['visible']:
            solution_counter += 1
        else:
            pass

print(f'The first solution is {solution_counter}\n')


# Solution for Part 2

for y_key in dict_grid.keys():
    for x_key in dict_grid[y_key].keys():
        list_scene = []
        if x_key == 1 or y_key == 1:
            dict_grid[y_key][x_key]['scene'] = 0
        elif x_key == x_dim or y_key == y_dim:
            dict_grid[y_key][x_key]['scene'] = 0
        else:
            scene_counter = 0
            for y in reversed(range(1, y_key)):
                if dict_grid[y][x_key]['height'] >= dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
                    break
                elif dict_grid[y][x_key]['height'] < dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
            list_scene.append(scene_counter)

            scene_counter = 0
            for y in range(y_key + 1, y_dim + 1):
                if dict_grid[y][x_key]['height'] >= dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
                    break
                elif dict_grid[y][x_key]['height'] < dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
            list_scene.append(scene_counter)

            scene_counter = 0
            for x in reversed(range(1, x_key)):
                if dict_grid[y_key][x]['height'] >= dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
                    break
                elif dict_grid[y_key][x]['height'] < dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
            list_scene.append(scene_counter)

            scene_counter = 0
            for x in range(x_key + 1, x_dim + 1):
                if dict_grid[y_key][x]['height'] >= dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
                    break
                elif dict_grid[y_key][x]['height'] < dict_grid[y_key][x_key]['height']:
                    scene_counter += 1
            list_scene.append(scene_counter)

            dict_grid[y_key][x_key]['scene'] = list_scene[0] * list_scene[1] * list_scene[2] * list_scene[3]

high_score = 0
for y_key in dict_grid.keys():
    for x_key in dict_grid[y_key].keys():
        if dict_grid[y_key][x_key]['scene'] > high_score:
            high_score = dict_grid[y_key][x_key]['scene']

print(f'The second solution is {high_score}')
