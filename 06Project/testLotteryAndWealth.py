import random
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib

def generateLotteryNumbers():
    """
    Returns a list of 5 random ints between 1 and 42, inclusive, with no
    duplicates.
    """
    mylist = []
    integer = random.randint(1, 42)
    for i in range(5):
        mylist.append(integer)
        integer = random.randint(1, 42)
    # print(mylist)
    return mylist

def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    print(my_list)
    print(lottery_list)
    count = 0
    for i in my_list:
        for j in lottery_list:
            if i == j:
                count += 1
    return count
    pass

def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    count = 0
    for i in my_list:
        for j in lottery_list:
            if i == j:
                count += 1
    return count
    pass


def playLottery():
    """
    Returns the reward after one lottery play.
    """
    my_list = generateLotteryNumbers()
    lottery_list = generateLotteryNumbers()
    count = countMatches(my_list, lottery_list)
    reward = 0
    if count <= 1:
        reward -= 1
    elif count == 2:
        reward += 1
    elif count == 3:
        reward += 11
    elif count == 4:
        reward += 198
    elif count == 5:
        reward += 212535
    
    return reward

def simManyPlays(n):
    """
    Function to graph the total winnings of a player who plays the lottery
    n times.
    Inputs: *n: The number of times the player enters the lottery.
    """
    winnings = []
    reward = 0
    for i in range(n):
        reward += playLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings)
    plt.legend()
    plt.show()

def main():

    simManyPlays(1000)
    # my_list = generateLotteryNumbers()
    # lottery_list = generateLotteryNumbers()
    # print(my_list)
    # print(lottery_list)
    # count = countMatches(my_list, lottery_list)
    # print(count)

    # generateLotteryNumbers()

if __name__ == "__main__":
    main()