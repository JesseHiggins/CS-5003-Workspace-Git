def averageGrades():
	
    num_inputs = 0
    total = 0
    grade = int(input("Enter your grade or -1 to quit: "))
                    
    while(grade >= 0 and grade <= 100):
        
        total += grade # total = total + grade 
        # += is shorthand that works in code. Which goes first and why?
        num_inputs += 1 #num_inputs = num_inputs + 1
        grade = int(input("Enter your grade or -1 to quit: "))
        
    average = total/num_inputs
    print("The average grade was:" + average)

def countByN(n, max = 100):
        '''Count by n
            params: n (the step counter), max - the highest
            returns: none
        '''
        start = n
        print(start)
        while(start < max):
            start += n # if you flip negative it will go to negative infinite loop
            print(start)

def main():
    countByN(3)

if __name__ == "__main__":
    main()
