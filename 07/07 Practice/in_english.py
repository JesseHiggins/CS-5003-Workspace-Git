def digit_to_english(digit):
    # Define a function to convert a single digit to its English representation
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return digit_words[digit]

def in_english(num):
    if num < 10:
        return digit_to_english(num)
    else:
        return in_english(num // 10) + " " + digit_to_english(num % 10)


def main():


    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    print(num[1])

if __name__ == "__main__":
    main()