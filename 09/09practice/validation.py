
def validation(negint, posfloat):

    if not isinstance(negint, int):
        raise ValueError("negint must be negative integer")
    if not isinstance(posfloat, float) or posfloat < 1000:
        raise ValueError("posfloat must be a positive float ")
    
    product = negint * int(posfloat)

    return product