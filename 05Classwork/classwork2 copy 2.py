
list = [1, 2, 3, 4, 5]

def multiply(list):
    location = 0
    while location < len(list):
        list[location] *= 5
        location += 1
    return list

def main():
    print(multiply(list))

main()

