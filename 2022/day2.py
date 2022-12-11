from typing import TextIO, List

def priority(letter:str)->int:
    """
    assigns a priority score to a letter.
    """
    if letter.isupper():
        score = ord(letter)-38 
    else:
        score = ord(letter)-96

    return score


def find_match(items:str)->str:
    """
    Find a match on both sides of a knapsack string.
    """
    half = len(items)//2
    left = sorted(list(set(items[0:half])))
    right = sorted(list(set(items[half:len(items)])))
    i = 0 
    j = 0

    match = None
    while not match:
        if left[i] == right[j]:
            match = left[i]
        elif left[i] < right[j]:
            i += 1
            if i == len(left)-1:
                # print('end')
                match = left[i] 
        else:
            j += 1
            if j == len(right)-1:
                # print('end')
                match = right[j] 

    # print("match ", left[i], right[j])
    return match



def find_badges(input_file:TextIO)->int:
    """
    Finds a match among three knapsacks for all knapsacks in the input.
    """
    knapsacks = [''] * 3
    total = 0
    for i, line in enumerate(input_file):
        elf_num = i % 3
        knapsacks[elf_num] = set(line.strip('\n'))
        if elf_num == 2:
            total += priority(list(knapsacks[0].intersection(knapsacks[1], knapsacks[2]))[0])
            

    return total 
        

    
with open('day2input.txt') as input:
    print(sum([priority(find_match(line.strip('\n'))) for line in input]))
    input.seek(0)   # Reset file stream to beginning of the file.
    print(find_badges(input))




