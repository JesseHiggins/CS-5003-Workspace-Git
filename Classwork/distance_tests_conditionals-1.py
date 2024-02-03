''' Jesse Higgins
    CS5001
    testing a function
'''
import rectanglecalc

def test_euclidean(expected):
        
    actual = euclidean(x1, y1, x2, y2)
    return abs(actual - expected) < EPSILON

def run_tests():

    num_fail = 0
    
    # Test 1: (0, 0), (0, 0). Expected: 0
    if (test_euclidean(0, 0, 0, 0, 0.0)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (2, -1), (-2, 2). Expected: 5
    if (test_euclidean(2, -1, -2, 2, 5.0)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    return num_fail
    
def main():
    print('Testing Euclidean distance functions...\n\n')
    failures = run_distance_tests()
    if failures == 0:
        print('Everything passed, great job functions!')
    else:
        print('Something went wrong, go back and fix pls.')
    

main()
