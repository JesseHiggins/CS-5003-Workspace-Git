''' Jesse Higgins
    CS5001
    Solution code for driver program
'''
import Task

class Task:
    ''' Class Task
        Attributes: title, due_date,
        Methods: mark_complete, change_date
    '''

    def __init__(self, title, due_date):
        '''
        Constructor -- creates new instances of Task
        Parameters:
           self -- the current object
           title -- the name of this task
           due_date -- the due date of this task
        '''
        self.title = title
        self.due_date = due_date

    def mark_complete(self):
        '''
        Method -- add elements to this coffee
        Parameters:
           self -- the current object
           adder -- the element to add
        '''
        self.title = f"{self.title} - Complete"

def main():
    
    #initialize title and due date variables with string values
    title = "Finish synthesis 03"
    due_date = "4/8"

    #Creates instance of task with attributes title and due date
    my_task = Task(title, due_date)

    #use dot notation to call method for my_task
    my_task.mark_complete()

if __name__ == "__main__":
    main()
    