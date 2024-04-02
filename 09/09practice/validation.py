
def validation(negint, posfloat):

    if not isinstance(negint, int):
        raise TypeError("negint must be negative integer")
    elif not negint < 0:
        raise ValueError("negint must be positive")
    elif not isinstance(posfloat, float):
        raise TypeError("posfloat must be a positive float ")
    elif not posfloat > 0:
        raise ValueError("posfloat must be positive")
    elif not posfloat < 1000:
        raise ValueError("posfloat must less than 1000")
    
    product = float(negint) * posfloat

    return product