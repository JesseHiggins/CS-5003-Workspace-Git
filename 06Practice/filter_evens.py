def filter_evens(list):
    evenlst = []
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            evenlst += [list[i]]
    return evenlst

def main():

    list = [1, 2, -3, 4, -5]
    print(filter_evens(list))

if __name__ == "__main__":
    main()