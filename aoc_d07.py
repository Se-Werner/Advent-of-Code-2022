# Day 7, Part 1 of Advent of Code


class Directory:
    all = []

    def __init__(self, name):                               # Initiate the Directory object
        self.name = name
        self.dir = []                                       # emtpy on init to be appended to later
        self.files = []                                     # empty on init to be appended to later

        Directory.all.append(self)

    def add_dir(self, dir_name):                            # Append the name string of a directory to objects list
        self.dir.append(dir_name)

    def add_file(self, file_name, file_size):               # Append the File object to the objects file list
        self.files.append(File(file_name, file_size))

    def calc_size(self, limit):                                    # Calculate the size of the Directory object
        total_size = 0                                      # Start with 0 for total size

        for x in self.files:                                # Adds the size of the File objects to total size
            total_size += x.size

        for y in self.dir:                                  # Loops through the directory names in object list
            for z in Directory.all:                         # Loops through all directory objects and
                if y == z.name:                             # searches for a match with the ones in the objects list
                    if z.calc_size(100_000) == 'HIGH':             # If the target directory's size is already over limit
                        return 'HIGH'                       # return a string instead of the size
                    else:
                        total_size += z.calc_size(100_000)         # If target directory is below limit, add size to total size

        if total_size > limit:                            # Checks if total size above limit, returns string if yes
            # print(total_size)
            return 'HIGH'
        elif total_size <= limit:                         # Returns the total size if it is below the limit
            # print(total_size)
            return total_size
        else:
            print("Error Total Size")

    def unlimited_size(self):
        total_size = 0                                      # Start with 0 for total size

        for x in self.files:                                # Adds the size of the File objects to total size
            total_size += x.size

        for y in self.dir:
            for z in Directory.all:
                if y == z.name:
                    total_size += z.unlimited_size()

        return total_size

    def __repr__(self):
        return f'dir({self.name})'


class File:
    all = []

    def __init__(self, name, f_size):                       # Initiates the File object with name and size
        self.name = name
        self.size = int(f_size)

        File.all.append(self)

    def __repr__(self):
        return f'File({self.name} / {self.size})'


with open('aoc_d07_input.txt') as file:                     # start of the program, reads the input file
    read_out = file.readlines()

lines_input = []
for line in read_out:                                       # cleans up the input lines and splits them on spaces
    clean = line.rstrip('\n')
    ready_line = clean.split(' ')
    lines_input.append(ready_line)

path = []
for line in lines_input:                                    # reads and processes the input lines
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':                             # If the input line is '$ cd ..' ignores it
                del path[-1]
            else:                                           # If input line is a 'cd *directory*',
                path.append(line[2])
                str_path = ''
                for el in path:
                    str_path += f'/{el}'
                dir_object = Directory(str_path)
        elif line[1] == 'ls':
            pass                                            # Ignores '$ ls' lines
        else:
            print(f'Error Command Read: {line[1]}')
    else:
        if line[0] == 'dir':                                # If the input line is a listed directory,
            str_path_child = str_path + f'/{line[1]}'
            dir_object.add_dir(str_path_child)              # appends its name to the current Directory Object
        else:
            dir_object.add_file(line[1], line[0])           # If input line is a File, adds it to current Directory Obj

solution = 0
for dir_item in Directory.all:                              # Loops through all directories
    size = dir_item.calc_size(100_000)                             # Calculates the size of the current directory
    if size == 'HIGH':                                      # Checks if the returned size is a string (hence over limit)
        pass
    else:
        solution += size                                    # Adds directory size to solution if it is not too high


print(f'The first solution is: {solution}\n')               # Prints solution


# Solution for Part 2

free_space = 70_000_000 - Directory.all[0].unlimited_size()
needed_space = 30_000_000 - free_space

sol_list = []
for dir_item in Directory.all:
    size = dir_item.unlimited_size()
    if size == 'HIGH':
        pass
    else:
        sol_list.append(size)

sol_list.sort()
for score in sol_list:
    if score >= needed_space:
        solution = score
        break
    else:
        pass

print(f'The second solution is {solution}')
