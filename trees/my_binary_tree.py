from binarytree import Node, show
import numpy.random as nprnd
# # binary search tree
# it can only have a maximum of two children --> hence binary
# one path to each node

# below is a simple tree that we will alter
# we need to add a right and left point, since binary search trees can only have two children per node
# left node child must be less than parent
# right node child must be more than or equal to parent

class MyBinaryTreeNode(Node):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.left = None
        self.right = None
    
    def add(self,new_node):
        if new_node.value >= self.value:
            # do something - either go to the right or become new_node
            if self.right is None:
                self.right = new_node
                new_node.parent = self
            else:
                self.right.add(new_node)
        else:
            # do something else
            if self.left is None:
                self.left = new_node
                new_node.parent = self
            else:
                self.left.add(new_node)

    def exists(self,value_to_search_for):
        if self.value == value_to_search_for:
            return True
        else:
            if value_to_search_for > self.value:
                # go to the right
                if self.right == None:
                    # end of tree
                    return False
                else:
                    return self.right.exists(value_to_search_for)
            else:
                # go to the left
                if self.left == None:
                    return False
                else: 
                    return self.left.exists(value_to_search_for)
                

class BST:
    def __init__(self):
        self.root = None
    
    def add(self,value):
        new_node = MyBinaryTreeNode(value)
    
        if self.root is None:
            self.root = new_node
        else:
            # this is MyBinaryTreeNode add method
            self.root.add(new_node)
    def exists(self,value):
        # return tree if the value exists in the tree, false otherwise
        if self.root is None:
            return False
        else:
            return self.root.exists(value)

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
for i in random_numbers(25):
    tree.add(i)
show(tree.root)



