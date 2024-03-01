def calculate_average(list):
    sum = 0
    average = 0
    for i in range(0, len(list)):
        if list == []:
            average = 0
        else:
            sum += list[i]
    if list != []:
        average = sum / (len(list))
    return average

def main():

    list = [1, 2, 3, 4, 5]
    print(calculate_average(list))

if __name__ == "__main__":
    main()