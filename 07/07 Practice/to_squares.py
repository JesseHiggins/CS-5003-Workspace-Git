def to_squares(list, index):

    if index < len(list):
        list[index] **= 2
        to_squares(list, index + 1)
    return list

def main():

    list = [1, 2, 3, 4, 5]
    print(to_squares(list, 1))
          
if __name__ == "__main__":
    main()