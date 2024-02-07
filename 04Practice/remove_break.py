
def main():
    a = 0
    b = 1
    c = b
    print("0\n1")
    while c < 1000:
        c = a + b
        print(c)
        a = b
        b = c


if __name__ == "__main__":
    main()
