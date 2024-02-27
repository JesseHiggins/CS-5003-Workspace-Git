def count_down():
    for i in range(100, -1, -5):
        if i == 0:
            print("Blastoff!")
        else:
            print(i)

def main():

    count_down()

if __name__ == "__main__":
    main()