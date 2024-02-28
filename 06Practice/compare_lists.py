def compare_lists(list1, list2):
    count = 0
    list = []
    for i in range(0, len(list1)):
        for j in list2:
            if i == j:
                list += [list[i]]
    if list1 = list:
        return True

def main():

    list = [1, 2, -3, 4, -5]
    print(filter_evens(list))

if __name__ == "__main__":
    main()