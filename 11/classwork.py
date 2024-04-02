class Queue:
    def __init__(self, size):

        self.data = [0] * size
        self.end = 0

    def enqueue(self, item):

        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1

    def dequeue(self):
        if self.end <= 0:
            print("Empty!")
        self.first = self.data[0]
        del(self.data[0])
        self.end -= 1
        return self.first
    
    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
           self -- the current object
        '''
        for i in range(self.end - 1, -1, -1):
            print(self.data[i])

    def count(self):

        return self.end
    
    def peek(self):
        
        return self.data[self]

def main():
    ''' 
    Driver program that uses our stack so that we can see it working
    '''
    my_queue = Queue(5)
    while True:
        cmd = input("enqueue, dequeue, dump or exit? ")
        if cmd == "enqueue":
            val = input("Data to add? ")
            my_queue.enqueue(val)
        elif cmd == "dequeue":
            val = my_queue.dequeue()
            print("pop() returned --", val)
        elif cmd == "dump":
            my_queue.dump()
        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()