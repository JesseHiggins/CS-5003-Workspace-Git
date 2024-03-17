''' Jesse Higgins
    CS5001
    defining name class
'''


class Name:
    ''' Class Name
        Attributes: first_name, last_name, nick_name
        Methods: add_on
    '''

    def __init__(self, first_name, last_name):
        '''
        Constructor -- creates new instances of coffee
        Parameters:
           self -- the current object
           first_name -- the first name of the name
           last_name -- the last name
           nick_name -- the nickname default is first name
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = first_name
        self.full_name = self.first_name + " " + self.last_name

    def get_first_name(self):
        '''
        method -- return the first name
        parameters: self -- curent object
        returns: first_name
        '''
        return self.first_name
    
    def get_last_name(self):
        
        return self.last_name
    
    def get_full_name(self):

        return self.full_name
    
    def set_nick_name(self, nick_name):

        self.nick_name = nick_name

        return self.nick_name
    
    def get_nick_name(self):

        return self.nick_name
    
    def __str__(self):

        output = self.first_name + ' "' + self.nick_name + '" ' + self.last_name
    
        return output

def main():

    p = Name("Jesse", "Higgins")
    p.set_nick_name("Admiral")
    q = p.get_full_name
    print(p)
    # print(q)
    # print(p.full_name)
    # print(Name)

if __name__ == "__main__":
    main()