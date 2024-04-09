'''inclass recursion
    Jesse Higgins
    02/26/2024
'''

def recursive_factorial(n):

    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

def recur_fib(x):

    if x == 1:
        return 1
    elif x == 2:
        return 1
    return recur_fib(x-1) + recur_fib(x-2)

def lindsayfib(x):
    if x == 1 or x == 0:
        return 1
    #recursive calls and progress towads end case
    answer = lindsayfib(x-1) + lindsayfib(x-2)
    print(answer)
    return answer

def sum_up(x, y):

    if x == y:
        return x
    return x + sum_up(x+1, y)

def sum_down(x, y):
    if x == y:
        return x
    return sum_down(x, y-1) + y

# summation(2, 4) + (summation(3, 4) + summation(4, 4))

def mystery(n):
    print("Before", n)
    if n < 0:
        return 2 * n
    else:
        return mystery(n - 1) + n

def main():
    # print(recur_factorial(5))
    # print(recur_fib(4))
    # lindsayfib(5)
    # print(summation(2, 4))
    print(mystery(3))



if __name__ == "__main__":
    main()