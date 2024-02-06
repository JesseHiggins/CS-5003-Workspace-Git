def count():
    location = 0
    string = input("Input a string")
    count = 0
    while location < len(string):
        if string[location] == "a":
            count += 1
        location += 1
    return count

def main():
    print(count())

main()

