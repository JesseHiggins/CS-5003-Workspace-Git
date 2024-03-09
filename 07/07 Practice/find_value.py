def sum_values(list, index, string):
    print("Start", index, list[index])
    # if index < len(list) - 1:
    if list[index] == string:
            return string
    else:
        sum_values(list, index - 1, string)
    print("End", index)
    
    

def main():

    list = ["g", "t", "hi", "hello"]
    print(sum_values(list, 0, "hi"))
          
if __name__ == "__main__":
    main()