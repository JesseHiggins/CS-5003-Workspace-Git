''' Align Online
    CS5001
    Sample code -- example of implementing the Queue ADT.
                   In this version, uses a circular buffer
'''
import random

class Queue:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our queue
        '''
        self.data = ["<EMPTY>"] * size
        self.end = 0
        self.start = 0

    def enqueue(self, item):
        ''' enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        '''
        if (self.end + 1) % len(self.data) == self.start:
            print("Full!")
            return
        self.data[self.end] = item
        self.end = (self.end + 1) % len(self.data)

    def dequeue(self):
        ''' deqeuue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        '''
        if self.start == self.end:
            print("Empty!")
            return
        item = self.data[self.start]
        self.data[self.start] = "<EMPTY>"
        self.start = (self.start + 1) % len(self.data)
        return item

    def dump(self):
        ''' dump -- debugging method for the queue
        Parameters:
           self -- the current object
        '''
        print(self.data, "Start:", self.start, ", End:", self.end)

def random_number():
    '''
    Random number function to return a random number for tickets'''
    return random.randint(0, 2)

def tickets():
    ''' 
    Ticket program that uses our queue to simulate a queue at a business using tickets
    '''
    my_queue = Queue(100)
    people_queued = 0
    customer_served = 0
    for i in range(100):
        num_enqueue = random_number()
        if num_enqueue == 0:
            pass
        elif num_enqueue == 1:
            my_queue.enqueue("Customer")
            people_queued += 1
        elif num_enqueue == 2:
            my_queue.enqueue("Customer")
            my_queue.enqueue("Customer")
            people_queued += 2


        if my_queue.start != my_queue.end:
            my_queue.dequeue()
            people_queued -= 1
            customer_served += 1
            print("Customer Served: ", customer_served)
        elif my_queue.start == my_queue.end:
            print("No one in line")

    print("Total customers in line: ", people_queued)

    return customer_served, people_queued

def tickets_seed(queue_num):
    ''' 
    Ticket program for testing one specific seed that uses our queue to simulate a queue at a business using tickets
    '''
    my_queue = Queue(100)
    people_queued = 0
    customer_served = 0

    #this section handles the enqueue and print statements and counter variables
    for i in range(100):
        num_enqueue = queue_num
        if num_enqueue == 0:
            pass
        elif num_enqueue == 1:
            my_queue.enqueue("Customer")
            people_queued += 1
        elif num_enqueue == 2:
            my_queue.enqueue("Customer")
            my_queue.enqueue("Customer")
            people_queued += 2

        #this section handles the dequeue and print statements and counter variables
        if my_queue.start != my_queue.end:
            my_queue.dequeue()
            people_queued -= 1
            customer_served += 1
            print("Customer Served: ", customer_served)
        elif my_queue.start == my_queue.end:
            print("No one in line")

    print("Total customers in line: ", people_queued)

    return customer_served, people_queued



def main():

    tickets()

if __name__ == "__main__":
    main()
