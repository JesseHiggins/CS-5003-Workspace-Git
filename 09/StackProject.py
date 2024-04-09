''' Jesse Higgins
    CS5001
    Stack Project - using the module copy of a stack to implement a stack that reads in open and close brackets and pops and pushes accordingly.
'''


class Stack:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our stack
        '''
        self.data = [0] * size
        self.end = 0

    def push(self, item):
        ''' push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        '''
        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1

    def pop(self):
        ''' pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        '''
        if self.end <= 0:
            print("Empty!")
            return
        self.end -= 1
        return self.data[self.end]

    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
           self -- the current object
        '''
        for i in range(self.end - 1, -1, -1):
            print(self.data[i])

def bracket_stack():
    '''bracket_stack - Function for testing and importing
        Params: none
        returns: none
    '''
    my_stack = Stack(5)
    cmd = input("Enter brackets: ")
    for i in cmd:
        if i == "(":
            my_stack.push("(")
        elif i == "{":
            my_stack.push("{")
        elif i == "[":
            my_stack.push("[")
        elif i == "<":
            my_stack.push("<")
        elif i == ")":
            val = my_stack.pop()
            if val == "(":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == "}":
            val = my_stack.pop()
            if val == "{":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == "]":
            val = my_stack.pop()
            if val == "[":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == ">":
            val = my_stack.pop()
            if val == "<":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")

def main():
    '''
    Driver program that uses our stack so that we can see it working
    '''
    my_stack = Stack(5)
    cmd = input("Enter brackets: ")
    for i in cmd:
        if i == "(":
            my_stack.push("(")
        elif i == "{":
            my_stack.push("{")
        elif i == "[":
            my_stack.push("[")
        elif i == "<":
            my_stack.push("<")
        elif i == ")":
            val = my_stack.pop()
            if val == "(":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == "}":
            val = my_stack.pop()
            if val == "{":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == "]":
            val = my_stack.pop()
            if val == "[":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")
        elif i == ">":
            val = my_stack.pop()
            if val == "<":
                print("pop() returned --", val)
            else: 
                #INVALID STRING
                print("invalid string")


if __name__ == "__main__":
    main()
