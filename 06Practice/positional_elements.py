def positional_elements(list1):
    count = 0
    for i in list1:
        if list1[i - 1] == i:
            count += 1

    return count

def main():

    list = [1, 2, 3, 5, 6]
    print(positional_elements(list))

if __name__ == "__main__":
    main()