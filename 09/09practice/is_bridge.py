def is_bridge(course):

    if not isinstance(course, int):
        raise TypeError("Course must be integer")
    
    if course == 5001 or course == 5002 or course == 5003 or course == 5004 or course == 5005 or course == 5008 or course == 5009:
        return True
    else:
        return False