
with open('test.txt', 'r') as fh:
    stacks = {}
    rules = []
    for line in fh.readlines():
        if line.startswith(' ') or line.startswith('['): # Any line may have several whitespaces anywhere
            for num, crate in enumerate(line.strip().split(' ')):
                print(crate)
                if crate.isalpha():
                    print(crate)
                    exit()
                if num in stacks.keys():
                    stacks[num].append(crate)
                else:
                    stacks[num] = [crate]
        elif line.startswith('move'):
            amount, i_pos, f_pos = line.strip().split(' ')[1], line.split(' ')[3], line.strip().split(' ')[5]
            rules.append((amount, i_pos, f_pos))
print(stacks)
print(rules)
