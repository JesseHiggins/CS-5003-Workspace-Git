def make_string_set(string):

    print(string.split(','))

    list = string.split(', ')


    print(list)

    setlist = set(list)

    setlist.remove('')

    print(setlist)

    return setlist

def main():

    string = "Riya, Ture, Nolan, , Maria"

    make_string_set(string)

if __name__ == "__main__":
    main()