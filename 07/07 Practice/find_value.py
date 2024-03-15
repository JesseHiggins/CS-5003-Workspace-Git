def find_value(list, index, string):
    print("Start", index, list[index])
    # if index < len(list) - 1:
    if index < 0:
        return "no"
    elif list[index] == string:
            return "yes"
    else:
        return find_value(list, index - 1, string)
    
    

def main():

    list = ["g", "t", "hi", "hello"]
    index = len(list) - 1

    print(find_value(list, index, "t"))
          
if __name__ == "__main__":
    main()