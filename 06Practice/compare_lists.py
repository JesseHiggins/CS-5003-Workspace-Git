def compare_lists(list1, list2):
    list = []
    for i in list1:
        for j in list2:
            if i == j:
                list += [i]
    if list1 == list:
        return True
    else:
        return False

def main():

    list1 = [1, 2, 3, 12]
    list2 = [3, 2, 1, 5, 7]

    print(compare_lists(list1, list2))

if __name__ == "__main__":
    main()