import re

filename = '2023day2input.txt'
RED = 12
GREEN = 13
BLUE = 14
sum = 0
answer2 = 0


with open(filename) as file:
    for i,line in enumerate(file):
        reds = re.findall(r"(\d*)\Dred", line)
        greens = re.findall(r"(\d*)\Dgreen", line)
        blues = re.findall(r"(\d*)\Dblue", line)

        if all([int(v) <= RED for v in reds]) and all([int(v) <= GREEN for v in greens]) and all([int(v) <= BLUE for v in blues]):
            sum += (i + 1)

        answer2 += max([int(v) for v in reds]) * max([int(v) for v in greens]) * max([int(v) for v in blues])

print(f"sum of part 1 is {sum}. The answer for part 2 is {answer2}")
