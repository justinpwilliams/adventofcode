import re
from typing import List, Tuple, TextIO


def get_num_stacks(line:str)->int:
    return (len(line) + 1)//4  # Double // is integer division. This will initialize a list size, so we want int not float


def get_stack_row(line:str)->list:
    """
    Uses regex to split incoming line into crates on the different stacks and their stack location
    """
    pattern = re.compile('([A-Z])\s?|\s(\s)\s\s?')
    
    # test = pattern.findall('[F]     [G]')
    return pattern.finditer(line)

def build_stacks(input_file:TextIO):
    first_line = input_file.readline()   # Get first line. We'll use ths twice.
    stacks = [[] for _ in range(get_num_stacks(first_line))]   # Make a list with en ugh spots to hold all the stacks

    input_file.seek(0)

    blank_pattern = re.compile(r'\s+')

    for line in input_file:

        i = 0
        for crate in get_stack_row(line):
            value = crate[0]
            if not blank_pattern.match(value):
                stacks[i].insert(0, value)
            i += 1
    print(stacks)


    pass

with open('day5input.txt') as input:
    build_stacks(input)

