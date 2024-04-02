''' Lab7
    Jesse Higgins
    March 18 2024
    Simulate a random sleepwalker and analyze the output of analysis functions
    '''
import random

def rs():
    '''rs chooses a random step and returns it
        Note that a call to rs() requires parentheses
        Params: none
        Returns: none
    '''
    return random.choice([-1,1])

def rwpos(start, nsteps):
    '''returns the position of the sleepwalker after nsteps
        params: start, nsteps
        returns: position of the sleepwalker
    '''
    print("start is", start)
    if nsteps == 0:
        return start
    return rwpos(start - rs(), nsteps - 1)

def rwsteps(start, low, hi, nsteps = 0):
    '''simulate a random walk using rs() until reaches at or beyond low or hi
        params: start - integer parameter indicating starting position, low, hi
        returns: number of steps taken until the sleepwalker reachers at or beyond low or hi
    '''
    print("start|" + "_"*(start - low) + "^" + "_"*(hi - start) + "|end")
    if start <= low:
        return nsteps
    elif start >= hi:
        return nsteps
    return rwsteps(start - rs(), low, hi, nsteps + 1)

def rwposPlain(start, nsteps):
    '''returns the position of the sleepwalker after nsteps
        params: start, nsteps
        returns: position of the sleepwalker
    '''
    if nsteps == 0:
        return start
    return rwposPlain(start - rs(), nsteps - 1)

def avgSignedDiscplacement(numtrials):
    '''stores output of rwposPlain(0,100) numtrials times in a liast
        params: numtrials
        returns: average of rwposPlain results
    '''

    list = []
    list = [rwposPlain(0,100) for x in range(numtrials)]
    average = sum(list) / len(list)
    return average

def avgSquaredDiscplacement(numtrials):
    '''stores output of rwposPlain(0,100) numtrials times in a liast
        params: numtrials
        returns: average of rwposPlain results
    '''

    list = []
    list = [rwposPlain(0,100) ** 2 for x in range(numtrials)]
    average = sum(list) / len(list)
    return average

def main():

    print(avgSignedDiscplacement(100))
    print(avgSquaredDiscplacement(100))

if __name__ == "__main__":
    main()