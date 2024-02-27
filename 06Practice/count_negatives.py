def count_negatives(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] < 0:
            count += 1
    return count

def main():

    list = [1, 2, -3, 4, -5]
    print(count_negatives(list))

if __name__ == "__main__":
    main()