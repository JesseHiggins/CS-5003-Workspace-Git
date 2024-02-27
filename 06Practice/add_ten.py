def add_ten(list):
    for i in range(0, len(list)):
        list[i] += 10
    return list

def main():

    list = [1, 2, -3, 4, -5]
    print(add_ten(list))

if __name__ == "__main__":
    main()