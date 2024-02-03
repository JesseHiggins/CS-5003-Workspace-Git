#
# Fall 2024, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

def main():
    #User Input date by day, month, year and convert to int
    day = int(input("Enter day:"))
    month = int(input("Enter month:"))
    year = int(input("Enter year:"))

    #Determine season by if/elif statements and store value as "season"
    if month == 1 or month == 2:
        season = "Winter"
    elif month == 12 and day >= 21:
        season = "Winter"
    elif month == 3 and day < 19:
        season = "Winter"
    elif month == 3 and day >= 19:
        season = "Spring"
    elif month > 3 and month < 6:
        season = "Spring"
    elif month == 6 and day < 20:
        season = "Spring"
    elif month == 6 and day >= 20:
        season = "Summer"
    elif month > 6 and month < 9:
        season = "Summer"
    elif month == 9 and day < 22:
        season = "Summer"
    elif month == 9 and day >= 22:
        season = "Fall"
    else:
        season = "Fall"
    
    #Print season to user
    print("Season:", season)

if __name__ == "__main__":
    main()