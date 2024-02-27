

def list_to_string(list):
    index = 0
    strlist = ""
    if list == []:
        strlist = ""
    else:  
        while index < len(list) - 1:
            strlist += str(list[index]) + "\n"
            index += 1
        strlist += str(list[index])
        print(strlist)
    return strlist


def main():
    list = [1, 2, 3, 4]
    list_to_string(list)


if __name__ == "__main__":
    main()
