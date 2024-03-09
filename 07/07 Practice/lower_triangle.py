def lower_triangle(n, current = 1):

    if current <= n:
        print("*" * current)
        lower_triangle(n, current + 1)
                     
def main():

    lower_triangle(5)

if __name__ == "__main__":
    main()
   