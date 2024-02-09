

def add_spaces(word):
    index = 0
    spacedword = ""
    if word == "":
        spacedword = ""
    else:  
        while index < len(word) - 1:
            spacedword = spacedword + word[index] + "   "
            index += 1
        spacedword = spacedword + word[index]
    return spacedword


def main():

    print(add_spaces(""))


if __name__ == "__main__":
    main()
