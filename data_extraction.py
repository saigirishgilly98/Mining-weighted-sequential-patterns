import random


def rand_list(start, end, num):
    res = []

    for _ in range(num):
        val = random.uniform(start, end)
        res.append(val)

    res.sort()
    return res


text_file = open('sample.data', 'r')
lines = text_file.readlines()

original_lines = lines

print('\nInput :\n')
print(lines)

x = dict()
for i in range(len(lines)):
    line1 = list(lines[i].split())
    # print(line1)
    length = int(line1[0])
    line1.pop(0)

    lst = []

    for j in range(length):
        size_of_list_of_time = int(line1[0])
        # print(size_of_list_of_time)
        line1.pop(0)
        # print(line1)

        list_of_time = rand_list(0, 1000, 1)
        for k in range(size_of_list_of_time):
            line1.pop(0)
        # print(list_of_time)

        lst.append(list_of_time[0])

    lst.sort()

    # print(f'The list is \n{lst}')
    x[i] = lst[:]

print(x)

print(original_lines)

x2 = dict()

for i in range(len(original_lines)):
    line1 = list(original_lines[i].split())
    # print(line1)
    length = int(line1[0])
    # print(length)
    line1.pop(0)
    # print(line1)

    list_of_time = []

    for j in range(length):
        size_of_list_of_time = int(line1[0])
        # print(size_of_list_of_time)
        line1.pop(0)
        # print(line1)

        temp = ''
        for k in range(size_of_list_of_time):
            temp = temp + line1[0].zfill(4)
            line1.pop(0)

        list_of_time.append(temp)
    # print(f'This is list of time: \n{list_of_time}')
    x2[i] = list_of_time

print(f'\n\nTime Stamp\n{x}\n\nSequence\n{x2}')

database = dict()
for i in x.keys():
    if len(x[i]) > 1:
        database[str(i)] = []
        for j in range(len(x[i])):
            database[str(i)].append([x2[i][j], x[i][j]])

print(database.keys())
print(database)
