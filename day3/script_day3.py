import string

# test = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"
#
# test = test.split("\n")

# part 1
import string

with open('input.txt', 'r') as fh:
    input_file = [ line.strip() for line in fh.readlines() ]

alphabet_low = list(string.ascii_lowercase)
alphabet_up = list(string.ascii_uppercase)

priorities_lowcase = { letter:num for letter, num in zip(alphabet_low, range(1,27)) }
priorities_upcase = { letter.upper():num for letter, num in zip(alphabet_low, range(27,53)) }
# print(priorities_upcase, priorities_lowcase)

sum_priorities = 0

for item in input_file:
    first_item, second_item = item[:int(len(item)/2)], item[int(len(item)/2):]
    for letter in first_item:
        if letter in second_item:
            match = letter # letter appearing in both items
            break
    sum_priorities += priorities_upcase[match] if match in priorities_upcase.keys() else priorities_lowcase[match]
print("Part 1:", sum_priorities)

# part 2

group = []
counter = 0
sum_priorities = 0
common_item = []

for line in input_file:
    group.append(line.strip())
    counter += 1

    if counter % 3 == 0:
        # print('group', group)
        for letter in group[0]:
            common_item = [letter for rucksack in group if letter in rucksack]
            if len(common_item) == 3:
                item_type = common_item[0]
                break
        # print("common items", common_item)
        sum_priorities += priorities_upcase[item_type] if item_type in priorities_upcase.keys() else priorities_lowcase[item_type]
        group = []
        common_item = []
print("Part 2:", sum_priorities)
