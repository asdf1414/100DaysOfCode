################################################################################
# A unival tree (which stands for "universal value") is a tree where all 
# nodes under it have the same value. Given the root to a binary tree, 
# count the number of unival subtrees.
################################################################################

# couldn't solve problem

class Node:

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def print_tree(self):
        print(self.data)