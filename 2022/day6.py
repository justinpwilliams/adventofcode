from typing import TextIO

def find_start(input_file:TextIO, key_length:int)->int:
    """
    Finds the number after which the code starts.
    """
    line = []   # Empty list to hold incoming chars
    found = set() 
    end_of_line = 0

    while len(found) < key_length:
        line.append(input_file.read(1))
        end_of_line += 1   
        if end_of_line >= key_length:
            found = set(line[end_of_line-key_length:end_of_line])

    return end_of_line


with open('day6input.txt') as input_file:
    start = find_start(input_file, 4)
    print(start)
    input_file.seek(0)
    start = find_start(input_file, 14)
    print(start)
