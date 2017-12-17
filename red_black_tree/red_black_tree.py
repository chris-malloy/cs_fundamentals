from binarytree import Node, show
import numpy.random as nprnd
from collections import deque

class MyBinaryTreeNode(Node):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.left = None
        self.right = None

    def add(self, new_node):
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

    def exists(self, value_to_search_for):
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
    def height(self):
        if self.left is None and self.right is None:
            return 1
        # calculate height of left sub tree
        # calculate height of right sub tree
        # return larger number + 1

        # TODO figure the rest out
        if self.left is not None:
            left_subtree_height = self.left.height()
        if self.right is not None:
            right_subtree_height = self.right.height()

        if left_subtree_height > right_subtree_height:
            return left_subtree_height
        else:
            return right_subtree_height
    
    def switch(self):
        self.left,self.right = self.right,self.left
        if self.left is not None:
            self.left.switch()
        if self.right is not None:
            self.right.switch()
    
    # in order traversal --> L S R
    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print self.value

        if self.right is not None:
            self.right.print_in_order()

    # post order traversal --> L R S
    def print_pre_order(self):
        print self.value

        if self.left is not None:
            self.left.print_in_order()

        if self.right is not None:
            self.right.print_in_order()

    # pre order traversal --> S L R
    def print_post_order(self):
        if self.left is not None:
            self.left.print_in_order()

        if self.right is not None:
            self.right.print_in_order()

        print self.value

    def is_root(self):
        return self.parent is None

    def is_right_child(self):
        return self.value >= self.parent.value

    def is_left_child(self):
        if self.is_root(): return False
        return self.value < self.parent.value

    def rotate_left(self):
        print "Starting Left Rotation"

        # cannot perfrom rotate_left on root
        if self.is_root():
            return
        # cannot perform rotate_left on left child
        if self.is_left_child():
            return

        ogParent = self.parent
        ogRight = self.left
        pivot = self

        ogParent.parent = pivot
        pivot.left = ogParent

        ogParent.right = ogLeft
        ogLeft.parent = ogParent
        return ogParent

        # Step 0: Assign all the variables you'll be using
        # Step 0.5: Check to see if you can actually do the rotation
        #       a. Cannot rotate root.
        #       b. Can only left rotate a right child
        # Step 1: Pivot Becomes the ogParent's parent
        # Step 2: THe ogLeftChild of the pivot becomes right child of ogParent
        print "Done with Left rotation"
        pass

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = MyBinaryTreeNode(value)

        if self.root is None:
            self.root = new_node
        else:
            # this is MyBinaryTreeNode add method
            self.root.add(new_node)

    def exists(self, value):
        # return tree if the value exists in the tree, false otherwise
        if self.root is None:
            return False
        else:
            return self.root.exists(value)
    def height(self):
        if self.root is not None:
            return self.root.height()
        return 0

    def print_in_order(self):
        if self.root is not None:
            self.root.print_in_order()
    
    def print_level_order(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while len(queue) != 0:
            current_node = queue.popleft()
            print current_node.value

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

    def test_rotate():
        if self.root is None or self.root.right is None:
            return

        ogParent = self.root.right.left_rotate()

        if ogParent is self.root:
            self.root = ogParent.parentq

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

node = MyBinaryTreeNode(1)
tree = BST()
for i in random_numbers(25):
    tree.add(i)
# show(tree.root)
# tree.print_level_order()
node.rotate_left()
