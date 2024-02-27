# This functions checks for the equality of two strings
def equal(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b != "0":
        return False
    elif a == "0" and b == "0":
        return True
    elif a != "0" and b != "0":
        return equal(a[1:], b[1:])

# This functions checks for the inequality of two strings
def notEqual(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return True
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return notEqual(a[1:], b[1:])

# This functions checks if a is less or equal to b
def lessOrEqual(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return True
    elif a != "0" and b != "0":
        return lessOrEqual(a[1:], b[1:])

# This functions checks if a is greater or equal to b
def greaterOrEqual(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return False
    elif a != "0" and b != "0":
        return greaterOrEqual(a[1:], b[1:])

# This functions checks if a is less than b
def less(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b != "0":
        return True
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return less(a[1:], b[1:])

# This functions checks if a is greater than b
def greater(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return False
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return greater(a[1:], b[1:])