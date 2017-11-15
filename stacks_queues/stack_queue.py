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
        
class MyQueue:
    def __init__(self):
        self.queue1 = MyStack()
        self.queue2 = MyStack()
    
    def enqueue(self,new_element):
        if(len(self.queue2)=0):
            self.queue1.push(new_element)
        else:
            for i in range(len(self.queue2)):
                temp = self.queue2.pop()
                self.queue1.push(temp)
        self.queue1.push(new_element)
    
    def dequeue(self):
        if(len(self.queue1)=0):
            self.queue2.pop()
        else:
            for i in range(len(self.queue1))
                temp = self.queue1.pop()
                self.queue2.push(temp)
        self.queue2.pop()