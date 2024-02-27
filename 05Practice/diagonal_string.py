

def diagonal_string(word):
    index = 0
    diagstring = ""
    if word == "":
        diagstring = ""
    else:  
        while index < len(word) - 1:
            diagstring += word[index] + "\n" + " " + " " * index
            index += 1
        diagstring += word[index]
        print(diagstring)
    return diagstring


def main():

    diagonal_string("northeastern")


if __name__ == "__main__":
    main()
