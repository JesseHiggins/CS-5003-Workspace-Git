

def name_number(name):
    index = 0
    name = name.lower()
    namelist = list(name)
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","x","w","z"]
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    while index < len(name):
        j = 0
        while j <= 24:
            if namelist[index] == alpha[j]:
                namelist[index] = num[j]
            j += 1
        print(namelist)
        index += 1
    total = sum(namelist)
    print(total)
    return total


def main():

    name_number("a")


if __name__ == "__main__":
    main()
