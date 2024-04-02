''' Jesse Higgins
    3/25/2024
    Tests for 07 lab functions
'''
import Lab7RandomSleepwalker

def main():
    
    print("Expected result between -10 and 10")
    print(Lab7RandomSleepwalker.rwpos(0, 10))

    print("\nExpected result is 1")
    print(Lab7RandomSleepwalker.rwsteps(0, -1, 1))

    print("\nExpected result is between -2 and 2")
    print(Lab7RandomSleepwalker.avgSignedDiscplacement(100))

    print("\nExpected is between 50 and 150")
    print(Lab7RandomSleepwalker.avgSquaredDiscplacement(100))

if __name__ == "__main__":
    main()