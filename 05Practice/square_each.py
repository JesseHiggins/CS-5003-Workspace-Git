

def square_each(list):
    index = 0
    squared = []
    while index < len(list):
        squared += [list[index] ** 2]
        index += 1
    print(squared)
    return squared


def main():
    list = [1, 2, 3, 4]
    square_each(list)


if __name__ == "__main__":
    main()
