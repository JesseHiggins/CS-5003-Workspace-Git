def sum_values(list, index):
    if index == len(list) - 1:
        return list[index]
    return sum_values(list, index + 1) + list[index]

def main():

    list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sum_values(list, 0))
          
if __name__ == "__main__":
    main()