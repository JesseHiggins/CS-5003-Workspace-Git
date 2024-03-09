def sum_values(list, index):
    if index == len(list) - 1:
        return list[index]
    elif list[index] < sum_values(list, index + 1):
        return sum_values(list, index + 1)
    elif list[index] > sum_values(list, index + 1):
        return list[index]
    sum_values(list, index + 1)

def main():

    list = [1, 7, 3, 12, 5, 4, 2, 1000, 88, 55]
    print(sum_values(list, 0))
          
if __name__ == "__main__":
    main()