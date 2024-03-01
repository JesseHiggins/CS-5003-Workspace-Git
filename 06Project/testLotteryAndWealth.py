''' 06Project - testing functions for simulating a lottery
    Jesse Higgins
    CS5001
    2/25/2024
'''

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
    mylist = random.sample(range(1,42), 5)
    # print(mylist)
    return mylist

def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    count = 0
    for i in lottery_list:
        for j in my_list:
            if i == j:
                count += 1
    return count
    pass

# def countMatches(my_list, lottery_list):
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

def getDisparityMessage(highIncomeList, lowIncomeList, decade):
    """
    Returns a string that describes the percentages of wealth possessed by the
    higher income half and lower income half for any given year.
    Inputs: *highIncomeList: The list containing wealth values for the high
             income group.
            *lowIncomeList: The list containing wealth values for low income
             group.
            *decade: The current decade as an integer.
    """
    sumwealth = sum(highIncomeList) + sum(lowIncomeList)
    lowIncomePercent = (sum(lowIncomeList) / sumwealth) * 100
    highIncomePercent = (sum(highIncomeList) / sumwealth) * 100

    message = "Decade " + str(decade) + ": The high income group possesses " +\
        str(highIncomePercent) + "% of the community's wealth, while the low"\
        "income group possesses " + str(lowIncomePercent) +\
        "% of the community's wealth."

    return message

def simLottery(incomeList, numPlayers):
    """
    Simulates lottery play for a number of players from a given income group.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            * numPlayers: The number of players who will play the lottery.
    """
    for i in range(numPlayers):
        player = random.randint(1, numPlayers)
        incomeList[player - 1] += playLottery()
    pass

def awardScholarship(incomeList, awardTotal):
    """
    Redistributes funds from the lottery in the form of a $1 scholarship.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            *awardTotal: The total amount of lottery funds to be rewarded
             to members of this income group.
    """
    for i in range(awardTotal):
        recipient = random.randint(1, len(incomeList))
        incomeList[recipient - 1] += 1
    pass

def main():

    list1 = [1, 2, 3, 4]

    simLottery(list1, 4)

    print(list1)
    # list2 = [2, 4, 6, 8]

    # print(getDisparityMessage(list1, list2, 80))
    # simManyPlays(1000)
    # my_list = generateLotteryNumbers()
    # lottery_list = generateLotteryNumbers()
    # print(my_list)
    # print(lottery_list)
    # count = countMatches(my_list, lottery_list)
    # print(count)

    # generateLotteryNumbers()

if __name__ == "__main__":
    main()