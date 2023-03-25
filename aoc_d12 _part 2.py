import string


class HikeNode:
    all = []

    def __init__(self, coords, path=None):
        self.coords = coords
        self.path = path
        HikeNode.all.append(self)

    def del_node(self):
        HikeNode.all.remove(self)


LIST_LETTERS = string.ascii_lowercase


with open('aoc_d12_input.txt') as file:
    input_lines = file.readlines()


# prepare the dictionary containing the playing grid
dict_grid = {}
line_counter = 0
for line in input_lines:
    clean_line = line.rstrip('\n')

    dict_line = {}
    char_counter = 0
    for char in clean_line:
        if char == 'S':
            dict_line[char_counter] = 'Start'
        elif char == 'E':
            dict_line[char_counter] = 'End'
        else:
            dict_line[char_counter] = int(LIST_LETTERS.index(char))

        char_counter += 1

    dict_grid[line_counter] = dict_line
    line_counter += 1
    x_dim = char_counter

y_dim = line_counter


# finding the start node
for y_key in dict_grid.keys():
    for x_key in dict_grid[y_key].keys():
        if dict_grid[y_key][x_key] == 'Start' or dict_grid[y_key][x_key] == 0:
            point = (x_key, y_key)
            start_node = HikeNode(point, [point])
        else:
            pass

run_state = True
step_counter = 1
while run_state:
    list_nodes_now = HikeNode.all.copy()

    print(f'Step {step_counter} - checking {len(list_nodes_now)} nodes')

    master_path = []
    for old_node in list_nodes_now:
        master_path = list(set(master_path + old_node.path))

    check_list = []
    for current_node in list_nodes_now:
        current_coords, current_path = current_node.coords, current_node.path
        # print(current_coords)

        if dict_grid[current_coords[1]][current_coords[0]] == 'End':
            check_list.append('y')
        else:
            check_list.append('x')
            target_coords_1 = (current_coords[0], current_coords[1] - 1)
            target_coords_2 = (current_coords[0] + 1, current_coords[1])
            target_coords_3 = (current_coords[0], current_coords[1] + 1)
            target_coords_4 = (current_coords[0] - 1, current_coords[1])
            list_targets = [target_coords_1, target_coords_2, target_coords_3, target_coords_4]

            for target in list_targets:
                if target[0] < 0 or target[0] > x_dim - 1:
                    pass
                elif target[1] < 0 or target[1] > y_dim - 1:
                    pass
                elif target in master_path:
                    pass
                elif dict_grid[target[1]][target[0]] == 'Start':
                    pass
                elif dict_grid[target[1]][target[0]] == 'End':
                    if dict_grid[current_coords[1]][current_coords[0]] >= 24:
                        new_path = current_path.copy()
                        new_path.append(target)
                        master_path.append(target)
                        new_node = HikeNode(target, new_path)
                    else:
                        pass
                elif dict_grid[current_coords[1]][current_coords[0]] == 'Start':
                    if dict_grid[target[1]][target[0]] <= 1:
                        new_path = current_path.copy()
                        # print(current_path)
                        new_path.append(target)
                        master_path.append(target)
                        new_node = HikeNode(target, new_path)
                        # print('Debug Start Success', new_path)
                    else:
                        pass
                elif dict_grid[current_coords[1]][current_coords[0]] + 1 >= dict_grid[target[1]][target[0]]:
                    new_path = current_path.copy()
                    new_path.append(target)
                    master_path.append(target)
                    new_node = HikeNode(target, new_path)
                    # print('\nDebug Success')
                    # print(target, ' ', dict_grid[target[1]][target[0]])
                    # print(current_coords, ' ', dict_grid[current_coords[1]][current_coords[0]], '\n')
                elif dict_grid[current_coords[1]][current_coords[0]] + 1 < dict_grid[target[1]][target[0]]:
                    pass
                else:
                    print('\nError pathfinding')
                    print(target, ' ', dict_grid[target[1]][target[0]])
                    print(current_coords, ' ', dict_grid[current_coords[1]][current_coords[0]], '\n')

            current_node.del_node()
            # print('\nNew Node')

    if 'y' in check_list:
        run_state = False

    step_counter += 1

answer_1 = 1_000_000
for final_node in HikeNode.all:
    if len(final_node.path) < answer_1:
        answer_1 = len(final_node.path)
        final_path = final_node.path


print(f'\nThe answer to part 1 is {answer_1 - 1} steps')
# print(final_path)
