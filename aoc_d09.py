# Day 9, Part 1 of Advent of Code 2022

def head_move(direction):
    global head_pos
    if direction == 'U':
        head_pos[1] += 1
    elif direction == 'D':
        head_pos[1] -= 1
    elif direction == 'R':
        head_pos[0] += 1
    elif direction == 'L':
        head_pos[0] -= 1
    else:
        print(f'Error Head Movement: {direction}')


def tail_check():
    global head_pos
    global tail_pos

    if head_pos[1] - tail_pos[1] == 2:
        tail_pos[1] += 1
        if head_pos[0] - tail_pos[0] == 0:
            pass
        else:
            tail_pos[0] = head_pos[0]

    elif tail_pos[1] - head_pos[1] == 2:
        tail_pos[1] -= 1
        if head_pos[0] - tail_pos[0] == 0:
            pass
        else:
            tail_pos[0] = head_pos[0]

    elif head_pos[0] - tail_pos[0] == 2:
        tail_pos[0] += 1
        if head_pos[1] - tail_pos[1] == 0:
            pass
        else:
            tail_pos[1] = head_pos[1]

    elif tail_pos[0] - head_pos[0] == 2:
        tail_pos[0] -= 1
        if head_pos[1] - tail_pos[1] == 0:
            pass
        else:
            tail_pos[1] = head_pos[1]

    else:
        pass


with open('aoc_d09_input.txt') as file:
    inputs = file.readlines()

inputs_clean = []
for l in inputs:
    line = l.rstrip('\n')
    line = line.split(' ')
    inputs_clean.append(line)

head_pos = [1000, 1000]
tail_pos = [1000, 1000]
list_tail_pos = ['10001000']

for command in inputs_clean:
    for numb in range(1, int(command[1])+1):
        head_move(command[0])
        tail_check()
        list_tail_pos.append(str(tail_pos[0]) + str(tail_pos[1]))

list_sol = list(set(list_tail_pos))
solution = len(list_sol)

print(f'The first Solution is {solution}\n')

# Solution for Part 2


class Node:
    all = []

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

        Node.all.append(self)

    def move(self, direction):
        if direction == 'U':
            self.y_pos += 1
        elif direction == 'D':
            self.y_pos -= 1
        elif direction == 'R':
            self.x_pos += 1
        elif direction == 'L':
            self.x_pos -= 1
        else:
            print(f'Error Node Movement: {direction}')

    def pos_check(self, index):
        if list_nodes[index-1].y_pos - self.y_pos == 2:
            self.y_pos += 1
            if abs(list_nodes[index-1].x_pos - self.x_pos) == 2:
                self.x_pos += int((list_nodes[index-1].x_pos - self.x_pos) / 2)
            else:
                self.x_pos = list_nodes[index-1].x_pos

        elif self.y_pos - list_nodes[index-1].y_pos == 2:
            self.y_pos -= 1
            if abs(list_nodes[index - 1].x_pos - self.x_pos) == 2:
                self.x_pos += int((list_nodes[index - 1].x_pos - self.x_pos) / 2)
            else:
                self.x_pos = list_nodes[index-1].x_pos

        elif list_nodes[index-1].x_pos - self.x_pos == 2:
            self.x_pos += 1
            if abs(list_nodes[index - 1].y_pos - self.y_pos) == 2:
                self.y_pos += int((list_nodes[index - 1].y_pos - self.y_pos) / 2)
            else:
                self.y_pos = list_nodes[index-1].y_pos

        elif self.x_pos - list_nodes[index-1].x_pos == 2:
            self.x_pos -= 1
            if abs(list_nodes[index - 1].y_pos - self.y_pos) == 2:
                self.y_pos += int((list_nodes[index - 1].y_pos - self.y_pos) / 2)
            else:
                self.y_pos = list_nodes[index-1].y_pos

        return [self.x_pos, self.y_pos]


list_nodes = []
for y in range(1, 11):
    node = Node(1000, 1000)
    list_nodes.append(node)

end_pos = []
for command in inputs_clean:
    for numb in range(1, int(command[1]) + 1):
        list_nodes[0].move(command[0])
        for z in range(1, 10):
            new_pos = list_nodes[z].pos_check(z)
            if z == 9:
                end_pos.append(str(new_pos[0]) + str(new_pos[1]))

list_sol = list(set(end_pos))
solution = len(list_sol)

print(f'The second Solution is {solution}\n')
