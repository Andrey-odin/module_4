from math import inf
def divide (first, second):
    try:
        a=first/second
        if second !=0:
            return a
    except ZeroDivisionError as e:
        return inf