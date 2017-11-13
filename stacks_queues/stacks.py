class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,new_element):
        #adds the new element to the end of our array
        self.queue.append(new_element)
        pass

    def dequeue(self):
        # Removes the first element from the array and returns
        temp = self.queue[0]
        del self.queue[0]
        return temp


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print q.dequeue()
print q.queue


# stacks are a logical structure to organize data.  great for programming
# LIFO --> Last In First Out

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        # Add the new element to the top of the stack
        self.stack.append(element)
        pass

    def pop(self):
        #Remove the top most element and also return it
        last_index = len(self.stack) - 1
        element = self.stack[last_index]
        del self.stack[last_index]
        return element


    def peek(self):
        # Return the top most element
        pass

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.peek()

# print s.stack
