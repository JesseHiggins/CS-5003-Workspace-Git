def max_helper(list, index):

    if len(list) == 1:
        return list[0]
    elif max_helper(list, index + 1) > max_helper(list, index + 2):
        return max_helper(list, index + 1)

def main():

    list = [1, 7, 3, 12, 5, 4, 2, 1000, 88, 55]
    print(max_helper(list, 0))
          
if __name__ == "__main__":
    main()