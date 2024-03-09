def upper_triangle(n):

    if n > 0:
        print("*" * n)
        upper_triangle(n-1)
                     
def main():

    upper_triangle(5)

if __name__ == "__main__":
    main()
   