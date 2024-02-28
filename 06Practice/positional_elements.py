def positional_elements(list1):
    count = 0
    for i in range(len(list1)):
        print(list1[i])
        if list1[i] == i:
            count += 1

    return count

def main():

    list = [5, 4, 3, 2, 1, -1]
    print(positional_elements(list))

if __name__ == "__main__":
    main()