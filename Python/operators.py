# Some of the following definitions will rely on methods from the file "relationalOperators.py"
# The following functions define the basic arithmetic operations of addition, multiplication, subtraction, division and modulo for the Peano numbers.

# These functions will use the built-in relational operators of Pyhton and won't rely on the ones defined in "relationalOperators.py"

def addition(a, b):
    if b == "0":
        return a
    else:
        return(addition("s" + str(a), b[1:]))
    
def multiplication(a, b):
    if b == "0":
        return 0
    else:
        return(addition(multiplication(str(a), b[1:]), str(a)))

def subtraction(a, b):
    if b == "0":
        return a
    elif a == "0" and b != "0":
        return "NOT DEFINED!"
    elif a != "0" and b != "0":
        return(subtraction(a[1:], b[1:]))

def division(a, b):
    if b == "0":
        return "NOT DEFINED!"
    elif a.count("s") < b.count("s"):
        return "0"
    elif a.count("s") >= b.count("s"):
        return ("s" + division(subtraction(a, b), b))
    
def modulo(a, b):
    if b == "0":
        return "NOT DEFINED!"
    elif a.count("s") < b.count("s"):
        return str(a)
    elif a.count("s") >= b.count("s"):
        return(modulo(subtraction(a, b), b))

## The following definitions in comments will rely on methods from the file "relationalOperators.py"!!!

# These functions will not use the built-in relational operators of Pyhton but the ones defined in "relationalOperators.py"

# def addition2(a, b):
#     if equal(b, "0"):
#         return a
#     else:
#         return(addition("s" + str(a), b[1:]))
    
# def multiplication2(a, b):
#     if equal(b, "0"):
#         return 0
#     else:
#         return(addition(multiplication(str(a), b[1:]), str(a)))

# def subtraction2(a, b):
#     if equal(b, "0"):
#         return a
#     elif equal(a, "0") and not equal(b, "0"):
#         return "NOT DEFINED!"
#     elif not equal(a, "0") and not equal(b, "0"):
#         return(subtraction(a[1:], b[1:]))
    
# def division2(a, b):
#     if equal(b, "0"):
#         return "NOT DEFINED!"
#     elif less(a, b):
#         return "0"
#     elif greaterOrEqual(a, b):
#         return ("s" + division(subtraction(a, b), b))

# def modulo2(a, b):
#     if equal(b, "0"):
#         return "NOT DEFINED!"
#     elif greater(b, a):
#         return str(a)
#     elif greaterOrEqual(a, b):
#         return(modulo(subtraction(a, b), b))

# Test cases 
# These will not include test cases for the definitions that rely on methods from the file "relationalOperators.py"
    
print("Addition:")
print("sssss0 + sss0: " + addition("sssss0", "sss0"))

print("\nMultiplication:")
print("sssss0 * sss0: " + multiplication("sssss0", "sss0"))

print("\nSubtraction:")
print("sssss0 - sss0: " + subtraction("sssss0", "sss0"))

print("\nDivision:")
print("sssss0 / sss0: " + division("sssss0", "sss0") + ", Rest: " + subtraction("sssss0", multiplication("sss0", division("sssss0", "sss0"))))

print("\nModulo:")
print("sssss0 / sss0: " + modulo("sssss0", "sss0")) # 2
print("sssss0 / sssss0: " + modulo("sssss0", "sssss0")) # 0
print("sssss0 / ssssss0: " + modulo("sssss0", "ssssss0")) # sssss0
print("sssss0 / 0: " + modulo("sssss0", "0")) # NOT DEFINED!
