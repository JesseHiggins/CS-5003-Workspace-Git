def find_max(list, index):
    if index == len(list) - 1:
        return list[index]
    elif list[index] < find_max(list, index + 1):
        return find_max(list, index + 1)
    elif list[index] > find_max(list, index + 1):

def main():
    
    index = 0
    list = [1, 2, 3, 4, 5]
    print(find_max(list, index))
          
if __name__ == "__main__":
    main()