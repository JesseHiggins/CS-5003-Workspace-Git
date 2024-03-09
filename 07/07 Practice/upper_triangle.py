def upper_triangle(n):

    if n == 1:
        answer = "*" 
    else:
        answer = upper_triangle(n-1) * "*"
        
    print(answer)
                     
def main():

    upper_triangle(5)

if __name__ == "__main__":
    main()
   