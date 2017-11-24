# most commonly used data structure for mysql
# very quick
# a tree is a set of nodes where there is one path from the root to any other children
# parent - can have as many children as they want
# children - can only have one parent
# levels are measured in height
# leaves - children
# subtree - think of them like subparents
# depth - the level that a certain node is on.
# a parent has pointers to it's children and it's parent

# below is a basic instance of a tree
class MyTreeNode():
    def __init__(self,value):
        self.value = value
        # children
        self.children = []
        self.parent = None

    def add_child(self,child_node):
        self.children.append(child_node)
        child_node.parent = self

    def remove_child(self,child_node):
        del self.children[self.children.indexof(child_node)]    

root = MyTreeNode(5)
root.add_child(MyTreeNode(10))
root.add_child(MyTreeNode(20))

for child in root.children:
    print child.value

# binary search tree
# it can only have a maximum of two children --> hence binary
# one path to each node




