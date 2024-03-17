def find_value(list, string):
    
    if list[0] == string:
        return True
    elif len(list) == 1:
        return False
    else: return find_value(list[1:], string)
    
    

def main():

    list = ["g", "t", "hi", "hello"]
    index = len(list) - 1

    print(find_value(list, "tg"))
          
if __name__ == "__main__":
    main()