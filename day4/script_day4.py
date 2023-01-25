
with open('test.txt', 'r') as fh:
    test = [ (line.strip().split(',')[0], line.strip().split(',')[1]) for line in fh.readlines() ]
with open('input.txt', 'r') as fh:
    input = [ (line.strip().split(',')[0], line.strip().split(',')[1]) for line in fh.readlines() ]
# print(test)

def overlap_assignment(part:str):
    counter = 0
    for pair in input:
        elf1_start, elf1_end = int(pair[0].split('-')[0]), int(pair[0].split('-')[1])
        elf2_start, elf2_end = int(pair[1].split('-')[0]), int(pair[1].split('-')[1])
        if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf2_start <= elf1_start and elf2_end >= elf1_end):
            counter += 1
        elif elf1_end < elf2_start or elf2_end < elf1_start:
            pass
        else:
            if part == 'part1':
                counter += 0
            elif part == 'part2':
                counter += 1
    return counter

print("Part 1: ", overlap_assignment('part1'))
print("Part 2: ", overlap_assignment('part2'))
