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
        if line == '\n':
            print('end of stack')
            break
        i = 0
        for crate in get_stack_row(line):
            value = crate[0]
            if not blank_pattern.match(value):
                stacks[i].insert(0, value)
            i += 1
    return stacks


def make_move(move:str, stacks)->None:
    """
    Executes a single move given a move strong of the form 
    'move num from stack to stack'
    """
    input_pattern = re.compile('[0-9]+')
    move_tuple = input_pattern.findall(move)
    num = int(move_tuple[0])
    from_stack = int(move_tuple[1])
    to_stack = int(move_tuple[2])

    # print(stacks[from_stack-1])
    # print(stacks[to_stack-1])
    # j = input('Enter to continue.')
    
    for i in range(num):
        stacks[to_stack-1].append(stacks[from_stack-1].pop())

    # print(move)
    # print(stacks[from_stack-1])
    # print(stacks[to_stack-1])


def make_moves(input_file:TextIO, stacks):
    for line in input_file:
        make_move(line, stacks)


def get_stack_tops(stacks)->None:
    message = ''
    for stack in stacks:
        message += stack[-1]
    print(stacks)
    print(message)


with open('day5input.txt') as input_file:
    stacks = build_stacks(input_file)
    make_moves(input_file, stacks)
    get_stack_tops(stacks)

