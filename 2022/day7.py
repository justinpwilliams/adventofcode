from typing import Type

class Node:
    size = 0
    name = None
    children = []

    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_child(self, name_to_find:str, size=0):
        found = False
        child_i = 0
        children_count = len(self.children)

        while found is not True:
            if child_i == children_count:
                self.children.append(Node(name_to_find, size))
                found = True
            elif self.children[child_i].get_name() == name_to_find:
                found = True
            else:
                child_i += 1

        return self.children[child_i]



def id_command(line:str):
    command_pattern = re.compile("([0-9]+|\$|dir)\s")




# Driver
# if ls, then id or add children until next ls or cd
# if cd and dir name, find child, go to that
# if cd .., return from recursive frame, maybe keep sum as we return
# if cd /, return all the way to top, read next line
# In other words...
# if number or dir, create it, stay in same frame
# if cd, change frame
# if ls, add or find until next $


if __name__ == "__main__":
    home = Node('home', 0)
    first = home.get_child('first', 100)
    print(first.get_name(), first.get_size())
