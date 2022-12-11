def compare_pairs(line:str)->bool:
    ids = [int(zone.strip('\n')) for elf in line.split(',') for zone in elf.split('-')]
    return ((ids[0] >= ids[2]) and (ids[1] <= ids[3])) or ((ids[2] >= ids[0]) and (ids[3] <= ids[1]))


def compare_pairs_2(line:str)->bool:
    ids = [int(zone.strip('\n')) for elf in line.split(',') for zone in elf.split('-')]
    cond1 = ids[0] >= ids[2] and ids[0] <= ids[3]    # first id contained in second group
    cond2 = ids[1] <= ids[3] and ids[1] >= ids[2]    # second id contained in second group
    cond3 = ids[2] >= ids[0] and ids[2] <= ids[1]    # first id contained in second group
    cond4 = ids[3] <= ids[1] and ids[3] >= ids[0]    # second id contained in second group
    return cond1 or cond2 or cond3 or cond4


with open('day3input.txt') as input:
    print(sum([compare_pairs(line) for line in input]))
    input.seek(0)
    print(sum([compare_pairs_2(line) for line in input]))

