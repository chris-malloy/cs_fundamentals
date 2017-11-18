class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def search(self, value):
        if self.value == value:
            return self

        if self.right is None:
            return None

        return self.right.search(value)

    def delete(self):
        previous_node = current_node.left
        next_node = current_node.right

        current_node.right = None
        current_node.left = None

        previous_node.right = next_node
        next_node.left = previous_node

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, value):
        new_node = LinkedListNode(value)

        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.right = new_node
            new_node.left = self.end
            self.end = new_node

    def search(self, value):
        if self.start is None:
            return None

        self.start.search(value)

    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False
    def has_only_one_node(self):
        if not self.is_empty() and self.start == self.end:
            return True
        else:
            return False

    def remove_last_node(self):
        if self.empty():
            return
        elif self.has_only_one_node():
            self.start = None
            self.end = None
        else:
            # remove the last object
            # STEP 1 remove the right pointer
            # STEP 2 remove the left pointer
            # STEP 3 remove the node
            second_to_last = self.end.left

            second_to_last.right = None
            self.end.left = None

            self.end = second_to_last


    def print_all_node_values(self):
        # Start with self.start
        # loop through all nodes
        # Print the value of each node
        current_node = self.start

        while current_node is not None:
            print current_node.value
            current_node = current_node.right

    def delete_at_index(self, index):
        current_node = self.start
        i = 0
        while current_node is not None:
            current_node = current_node.right
            i += 1
            if (i == index):
                node_i_want_to_delete = current_node
                break;

                current_node = current_node.right
                i += 1

            if node_i_want_to_delete == self.start
                self.start = node_i_want_to_delete.right
            
            if node_i_want_to_delete == self.end
                self.end = node_i_want_to_delete.left
            
            node_i_want_to_delete.delete()

  


            
            
        

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.print_all_node_values()

