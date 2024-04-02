def get_value_string(dictionary):

    values = dictionary.values()

    mystring = ''

    for k in values:
        mystring += '' + str(k) + '\n'
    
    if mystring.endswith('\n'):
        mystring = mystring[:-1]
        
    print(mystring)

    return mystring

def main():

    dictionary = {"Maria": "Associate Professor", "John" : "Clinical Instructor", "Carla" : "Dean of Khoury"}

    get_value_string(dictionary)

if __name__ == "__main__":
    main()