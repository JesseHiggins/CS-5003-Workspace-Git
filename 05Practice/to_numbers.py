

def to_numbers(list):
    index = 0
    squared = []
    while index < len(list):
        squared += [float(list[index])]
        index += 1
    print(squared)
    return squared


def main():
    list = ["1", "2", "3", "4"]
    to_numbers(list)


if __name__ == "__main__":
    main()
