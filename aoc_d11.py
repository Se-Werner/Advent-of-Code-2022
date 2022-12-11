# Day 11, part 1 of Advent of Code
import math
import sympy

TARGET_ROUND = 20


with open('aoc_d11_test.txt') as file:
    input_lines = file.readlines()

list_monkeys = []
dict_monkey = {}
if_counter = 0
for line in input_lines:
    ready_line = line.rstrip('\n').lstrip(' ').split(' ')

    if ready_line[0] == 'Monkey':
        pass

    elif ready_line[0] == 'Starting':
        item_list = []
        for i in ready_line[2:]:
            item_list.append(int(i.rstrip(',')))
        dict_monkey['items'] = item_list

    elif ready_line[0] == 'Operation:':
        dict_monkey['operator'] = ready_line[4]
        dict_monkey['factor'] = ready_line[5]

    elif ready_line[0] == 'Test:':
        dict_monkey['divisor'] = int(ready_line[3])

    elif ready_line[0] == 'If':
        if if_counter == 0:
            dict_monkey['true'] = int(ready_line[5])
            if_counter = 1
        elif if_counter == 1:
            dict_monkey['false'] = int(ready_line[5])
            if_counter = 0
            dict_monkey['active'] = 0
            list_monkeys.append(dict_monkey)
            dict_monkey = {}
        else:
            print('Error If counter')

    elif ready_line[0] == '':
        pass

    else:
        print('Error Line interpreter')

round_counter = 1
while round_counter <= TARGET_ROUND:
    for mk in list_monkeys:
        for item in mk['items']:
            if mk['factor'] == 'old':
                if mk['operator'] == '+':
                    new = item + item
                elif mk['operator'] == '*':
                    new = item * item
                else:
                    print('Error Operator 1')

            else :
                if mk['operator'] == '+':
                    new = item + int(mk['factor'])
                elif mk['operator'] == '*':
                    new = item * int(mk['factor'])
                else:
                    print('Error Operator 1')

            new = math.floor(new / 3)

            if new % mk['divisor'] == 0:
                list_monkeys[mk['true']]['items'].append(new)
            else:
                list_monkeys[mk['false']]['items'].append(new)

            mk['active'] += 1

        mk['items'] = []

    # mk_counter = 0
    # for mk in list_monkeys:
    #     print(f'{round_counter} / {mk_counter} - {mk["items"]}')
    #     mk_counter += 1
    # print('')
    # print(round_counter)
    round_counter += 1

high_scores = []
for mk in list_monkeys:
    if len(high_scores) <= 1:
        high_scores.append(mk['active'])
    elif len(high_scores) == 2:
        high_scores.sort()
        if mk['active'] > high_scores[0]:
            high_scores.append(mk['active'])
            del high_scores[0]
        else:
            pass
    else:
        print('Error high scores')

solution = high_scores[0] * high_scores[1]

print(f'The first solution is {solution}\n')


# Part 2 Solution

prime_num = list(sympy.primerange(2, 100_000_000))
prime_num.sort()


def factorize(numb):
    global prime_num
    # print(numb)

    if numb in prime_num:
        return [numb]
    else:
        for p_num in prime_num:
            if numb % p_num == 0:
                if int(numb / p_num) in prime_num:
                    return [p_num, int(numb / p_num)]
                else:
                    new_list = factorize(int(numb / p_num))
                    new_list.append(p_num)
                    return new_list
            else:
                pass

    print(f'Error Factorize: {numb}')


def defactorize(f_dict):
    num = 1
    for x in f_dict.keys():
        y = int(x) ** f_dict[x]
        new_num = y * num
        num= new_num

    return num


list_monkeys = []
dict_monkey = {}
if_counter = 0
for line in input_lines:
    ready_line = line.rstrip('\n').lstrip(' ').split(' ')

    if ready_line[0] == 'Monkey':
        pass

    elif ready_line[0] == 'Starting':
        item_list = []
        for i in ready_line[2:]:
            dict_prime = {}
            factor_list = factorize(int(i.rstrip(',')))
            for p in factor_list:
                if str(p) in dict_prime.keys():
                    dict_prime[str(p)] += 1
                else:
                    dict_prime[str(p)] = 1
            item_list.append(dict_prime)
        dict_monkey['items'] = item_list

    elif ready_line[0] == 'Operation:':
        dict_monkey['operator'] = ready_line[4]
        dict_monkey['factor'] = ready_line[5]

    elif ready_line[0] == 'Test:':
        dict_monkey['divisor'] = int(ready_line[3])

    elif ready_line[0] == 'If':
        if if_counter == 0:
            dict_monkey['true'] = int(ready_line[5])
            if_counter = 1
        elif if_counter == 1:
            dict_monkey['false'] = int(ready_line[5])
            if_counter = 0
            dict_monkey['active'] = 0
            list_monkeys.append(dict_monkey)
            dict_monkey = {}
        else:
            print('Error If counter')

    elif ready_line[0] == '':
        pass

    else:
        print('Error Line interpreter')

for x in list_monkeys:
    print(x)

TARGET_ROUND = 1000 # 10_000
round_counter = 1
while round_counter <= TARGET_ROUND:
    for mk in list_monkeys:
        for item in mk['items']:
            if mk['factor'] == 'old':
                if mk['operator'] == '+':
                    for p_k in item.keys():
                        item[p_k] = item[p_k] * 2
                    new_dict = item
                elif mk['operator'] == '*':
                    for p_k in item.keys():
                        item[p_k] = item[p_k] * item[p_k]
                    new_dict = item
                else:
                    print('Error Operator 1')

            else :
                if mk['operator'] == '+':
                    new_dict = {}
                    factor_list = factorize(defactorize(item) + int(mk['factor']))
                    for p in factor_list:
                        if str(p) in new_dict.keys():
                            new_dict[str(p)] += 1
                        else:
                            new_dict[str(p)] = 1
                elif mk['operator'] == '*':
                    if mk['factor'] in item.keys():
                        item[mk['factor']] += 1
                    else:
                        item[mk['factor']] = 1
                    new_dict = item
                else:
                    print('Error Operator 2')

            if mk['divisor'] in new_dict.keys():
                list_monkeys[mk['true']]['items'].append(new_dict)
                print('yes')
            else:
                list_monkeys[mk['false']]['items'].append(new_dict)
                # print(f'{mk["divisor"]} - {new_dict}')

            mk['active'] += 1
            # print(mk['active'])

        mk['items'] = []

    # mk_counter = 0
    # for mk in list_monkeys:
    #     item_list = []
    #     for a in mk['items']:
    #         item_list.append(defactorize(a))
    #     print(f'{round_counter} / {mk_counter} - {item_list}')
    #     mk_counter += 1
    # print('')
    print(round_counter)
    round_counter += 1

high_scores = []
for mk in list_monkeys:
    print(mk['active'])
    if len(high_scores) <= 1:
        high_scores.append(mk['active'])
    elif len(high_scores) == 2:
        high_scores.sort()
        if mk['active'] > high_scores[0]:
            high_scores.append(mk['active'])
            del high_scores[0]
        else:
            pass
    else:
        print('Error high scores')

solution = high_scores[0] * high_scores[1]

print(f'The second solution is {solution}\n')