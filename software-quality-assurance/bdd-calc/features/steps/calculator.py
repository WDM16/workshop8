def add(a, b):
    return int(a) + int(b) 


def subtract(a, b):
    return int(a) - int(b) 

def multiply(a, b):
    return int(a) * int(b)

def divide(a, b):
    if(b > 0):
        return int(a) / int(b)
    else:
        raise Exception(u'THE Wrong calculation. Bug in code.')