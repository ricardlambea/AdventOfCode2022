# part 1
with open('input_day1.txt', 'r') as input_f:
    input_file = [ line.strip() for line in input_f.readlines()]

elf_cal = 0
elf_counter = 0
sum_calories = []

for calories in input_file:
    if calories == '':
        sum_calories.append(elf_cal)
        elf_cal = 0
    else:
        calories = int(calories)
        elf_cal += calories
else:
    sum_calories.append(elf_cal)
print(len(sum_calories))
print(max(sum_calories))


# part2
sum_calories.sort(reverse=True)
top3 = sum_calories[2]
top2 = sum_calories[1]
top1 = sum_calories[0]

print(top1+top2+top3)
