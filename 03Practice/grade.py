
import math


def grade(numgrade):

    if numgrade >= 0 and numgrade <= 64:
        grade = "F"
    if numgrade >= 65 and numgrade <= 68:
        grade = "C-"
    if numgrade >= 69 and numgrade <= 72:
        grade = "C"
    if numgrade >= 73 and numgrade <= 76:
        grade = "C+"
    if numgrade >= 77 and numgrade <= 81:
        grade = "B-"
    if numgrade >= 82 and numgrade <= 85:
        grade = "B"
    if numgrade >= 86 and numgrade <= 89:
        grade = "B+"
    if numgrade >= 90 and numgrade <= 92:
        grade = "A-"
    if numgrade >= 93 and numgrade <= 100:
        grade = "A"

    return grade


def main():

    result = grade(56)

    print(result)


if __name__ == "__main__":
    main()
