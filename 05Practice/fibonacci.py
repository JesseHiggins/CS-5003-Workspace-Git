

def fibonacci(num):
    index = 0
    num1 = 0
    num2 = 1
    next = num2
    fib = [num2]
    if num == 0:
        fib = []
    while index < num - 1:
        fib += [next]
        (num1, num2) = (num2, next)
        next = num1 + num2
        index += 1
    print(fib)
    return fib


def main():
    num = 10
    fibonacci(num)


if __name__ == "__main__":
    main()
