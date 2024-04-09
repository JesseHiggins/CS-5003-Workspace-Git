''' Jesse Higgins
    CS5001
    Solution code
'''

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

    def mark_complete(self, task):
        '''
        Method -- add elements to this coffee
        Parameters:
           self -- the current object
           adder -- the element to add
        '''
        self.title = f"{self.title} Complete"

    def __str__(self):
        '''
        Method -- returns a string that represents this task
        Parameters:
           self -- the current object
        '''
        output = "Title: " + self.title + "\n" \
                 "Due Date: " + self.due_date
                
        return output