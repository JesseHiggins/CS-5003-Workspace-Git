

def convert_tuple(tuple):
    index = 0
    tuplist = []
    if tuple == ():
        tuplist = []
    else:  
        while index < len(tuple) - 1:
            tuplist += [tuple[index]]
            index += 1
        tuplist += [tuple[index]]
        print(tuplist)
    return tuplist


def main():
    tuple = (1, 2, 3, 4)
    convert_tuple(tuple)


if __name__ == "__main__":
    main()
