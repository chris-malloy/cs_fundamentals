class LinkedListNode:
    def __init__(self, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, key, value):
        new_node = LinkedListNode(key, value)

        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.right = new_node
            new_node.left = self.end
            self.end = new_node

class MyHashTable:  
    def __init__(self):
        self.my_array = [None] * 26

    def put(self,key,value):
        index = self.my_hash_function(key)
        # self.my_array[index] = value
        if self.my_array[index] == None:
            self.my_array[index] = LinkedList()

        self.my_array[index].append(key, value)

    def get(self,key):
        index = self.my_hash_function(key)
        # return self.my_array[index]
        if self.my_array[index] is None:
            return None
            
        linked_list = self.my_array[index]

        current_node = linked_list.start

        while current_node != None:
            if current_node.key == key:
                return current_node 
            current_node = current_node.right

    def my_hash_function(self,input_value):
        #input will be word we are sending in
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        first_letter = input_value[0]
        return alphabet.index(first_letter)

hash_table = MyHashTable()
hash_table.put('first_name','Bob')
print hash_table.get('first_name').value



