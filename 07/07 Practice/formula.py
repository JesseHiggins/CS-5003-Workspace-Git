
def formula(n):
    if n == 1:
        return 3
    else:
        return 2 * formula(n - 1) + 5

def main():

    print(formula(1))
    print(formula(2))
    print(formula(3))


if __name__ == "__main__":
    main()
