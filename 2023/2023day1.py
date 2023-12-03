import re

filename = '2023day1input.txt'
sum = 0
sum2 = 0

spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open(filename) as file:
    for line in file:
        digits = re.findall(r"\d", line)
        if len(digits) > 1:
            sum += int(digits[0]) * 10 + int(digits[-1])
        else:
            sum += int(digits[0]) * 10 + int(digits[0])

        digits = []
        spelled_match = re.compile(r"\d|nine|eight|seven|six|five|four|three|two|one|zero")
        match = spelled_match.search(line)
        while match:
            digits.append(match.group())
            next = match.start() + 1
            match = spelled_match.search(line, next)

        # digits = re.findall(r"\d|nine|eight|seven|six|five|four|three|two|one|zero", line)
        digits = [spelled_digits[t] if len(t) > 1 else t for t in digits]
        if len(digits) > 1:
            sum2 += int(digits[0]) * 10 + int(digits[-1])
        else:
            sum2 += int(digits[0]) * 10 + int(digits[0])




print(f"The first part answer is {sum}. The second part answer is {sum2}")

