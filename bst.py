''' BINARY SEARCH TREES
Code written by GitHub User mxie220)'''

import time

def node(i):
    return [i, None, None]


def check_left(current_node, new):
    left = current_node[1]
    if left == None:
        new_node = node(new)
        current_node[1] = new_node
    else:
        check(left, new)
    return current_node

def check_right(current_node, new):
    right = current_node[2]
    if right == None:
        new_node = node(new)
        current_node[2] = new_node
    else:
        check(right, new)
    return current_node


def check(current_node, new):
    current = current_node[0]
    if new < current:
        check_left(current_node, new)
    if new > current:
        check_right(current_node, new)
    return current_node

def insert(current):
    new = int(input("Insert value: \n"))
    print("Please wait while we process your request...")
    time.sleep(2)
    tree = check(current, new)
    print(tree)
    repeat = input("\n\nDo you wish to add more to the tree? \n")
    while "y" in repeat.lower():
        insert(tree)
    return tree

def main():
    current = int(input("Enter root value: \n"))
    root = node(current)
    print(insert(root))


main()



