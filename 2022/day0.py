
with open("day0input.txt") as input:
    max_calories = 0
    calories = 0
    elf = 0
    for line in input:
        if line == "\n":
            max_calories = max(max_calories, calories)
            print("elf ", elf, " has ", calories, " calories.")
            elf += 1
            calories = 0
        else:        
            calories += int(line)

print(max_calories)





