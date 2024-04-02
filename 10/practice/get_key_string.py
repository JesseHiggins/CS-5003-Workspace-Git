def get_key_string(dictionary):

    keys = dictionary.keys()

    mystring = ''

    for k in keys:
        mystring += '' + str(k) + '\n'
    
    if mystring.endswith('\n'):
        mystring = mystring[:-1]
        
    print(mystring)

    return mystring

def main():

    dictionary = {"Maria": "Associate Professor", "John" : "Clinical Instructor", "Carla" : "Dean of Khoury"}

    get_key_string(dictionary)

if __name__ == "__main__":
    main()