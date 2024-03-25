'''classwork
    jesse higgins
    dictionaries etc
'''

class Student():

    def __init__(self):
        
        self.dictionary = {}

    def add(self, name, course):

        self.dictionary[name] = course

    def display(self):

        for k, v in self.dictionary.items():
            print(k, v)
        
    def delete(self, name):

        del self.dictionary[name]

class StudentList:

    def __init__(self):
        
        self.student_names = []
        self.student_course = []

    def add(self, name, number):

        self.student_names.append(name)
        self.student_course.append(number)

    def display(self):

        for i in range(0, len(self.student_names)):
            print(f"{self.student_names[i]} is in {self.student_course[i]}")
        
    def delete(self, name):

        location = self.student_names.index(name)

        self.student_names.remove(name)
        del self.student_course[location]

class Phonebook():

    def __init__(self):

        self.phonebook = {}

    def add(self, name, phone_number):

        self.phonebook[name] = phone_number

    def print_phone_book(self):
    
        for k, v in self.phonebook.items():
            print(k, v)
    
def print_phone_book(phonebook):

    for name in phonebook:
        print(name + ":" + str(phonebook[name]))
        print(name,phonebook[name])

def main():

    # # student_list = Student()

    # # student_list.add("Jesse", "CS5001")
    # # student_list.add("Jeff", "CS5001")
    # # student_list.add("Ham", "CS6000")

    # # student_list.display()

    # # student_list.delete("Ham")

    # # student_list.display()

    # SECOND PROJECT

    # student_list1 = StudentList()

    # student_list1.add("Jesse", "CS5001")
    # student_list1.add("Jeff", "CS5001")
    # student_list1.add("Ham", "CS6000")

    # student_list1.display()

    # student_list1.delete("Ham")

    # student_list1.display()

    # THIRD PROJECT

    # phonebook = {"Mom": 3175551234,
    #              "Dad": 8645554567,
    #              "Bro": 3125559876,
    #              "Sue": 2075553456}
    
    # print_phone_book(phonebook)
    # print(phonebook)
    # phonebook.pop("Sue")
    # print(phonebook)

    # phonebook = Phonebook()
    # phonebook.add("Mom", 3175551234)
    # phonebook.add("Dad", 8645554567)
    # phonebook.add("Bro", 3125559876)
    # phonebook.print_phone_book()

    names = ("Jesse, Emma, William, Bob, Rob, Jesse, Emma")
    setnamesbad = set(names)
    print(setnamesbad)
    listnames = names.split(", ")
    print(listnames)
    setnames = set(listnames)
    print(setnames)
if __name__ == "__main__":
    main()
