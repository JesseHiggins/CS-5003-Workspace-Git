def get_dictionary_string(dictionary):

    values = dictionary.values()
    keys = dictionary.values()

    mystring = ''

    for k,j in dictionary.items():
        mystring += '' + str(k) + " - " + str(j) + '\n'
    
    if mystring.endswith('\n'):
        mystring = mystring[:-1]
        
    print(mystring)

    return mystring

def main():

    dictionary = {"Maria": "Associate Professor", "John" : "Clinical Instructor", "Carla" : "Dean of Khoury"}

    get_dictionary_string(dictionary)

if __name__ == "__main__":
    main()