def add(a,b):
    if isinstance(a,(int, float)) and isinstance(b,(int, float)):
        return a+b
    return TypeError

def product(a,b):
        return a*b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a**b

