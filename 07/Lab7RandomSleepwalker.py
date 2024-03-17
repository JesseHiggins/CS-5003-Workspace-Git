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

def rwsteps(start, low, hi, nsteps):
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

def main():

    print(rwsteps(40, 35, 45, 0))

if __name__ == "__main__":
    main()