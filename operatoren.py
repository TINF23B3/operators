# Vergleichsoperatoren
def equal(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b != "0":
        return False
    elif a == "0" and b == "0":
        return True
    elif a != "0" and b != "0":
        return equal(a[1:], b[1:])

def notEqual(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return True
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return notEqual(a[1:], b[1:])

def lessOrEqual(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return True
    elif a != "0" and b != "0":
        return lessOrEqual(a[1:], b[1:])

def greaterOrEqual(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return False
    elif a != "0" and b != "0":
        return greaterOrEqual(a[1:], b[1:])

def less(a, b):
    if a != "0" and b == "0":
        return False
    elif a == "0" and b != "0":
        return True
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return less(a[1:], b[1:])

def greater(a, b):
    if a != "0" and b == "0":
        return True
    elif a == "0" and b != "0":
        return False
    elif a == "0" and b == "0":
        return False
    elif a != "0" and b != "0":
        return greater(a[1:], b[1:])


# Grundrechenarten
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

# Modifikation der Grundrechenarten mit den Funktionen der Vergleichsoperatoren
def addition2(a, b):
    if equal(b, "0"):
        return a
    else:
        return(addition("s" + str(a), b[1:]))
    
def multiplication2(a, b):
    if equal(b, "0"):
        return 0
    else:
        return(addition(multiplication(str(a), b[1:]), str(a)))

def subtraction2(a, b):
    if equal(b, "0"):
        return a
    elif equal(a, "0") and not equal(b, "0"):
        return "NOT DEFINED!"
    elif not equal(a, "0") and not equal(b, "0"):
        return(subtraction(a[1:], b[1:]))
    
def division2(a, b):
    if equal(b, "0"):
        return "NOT DEFINED!"
    elif less(a, b):
        return "0"
    elif greaterOrEqual(a, b):
        return ("s" + division(subtraction(a, b), b))

def modulo(a, b):
    if equal(b, "0"):
        return "NOT DEFINED!"
    elif greater(b, a):
        return str(a)
    elif greaterOrEqual(a, b):
        return(modulo(subtraction(a, b), b))

print("Addition:")
print("sssss0 + sss0: " + addition("sssss0", "sss0"))

print("Addition2:")
print("sssss0 + sss0: " + addition2("sssss0", "sss0"))

print("\nMultiplication:")
print("sssss0 * sss0: " + multiplication("sssss0", "sss0"))

print("\nMultiplication2:")
print("sssss0 * sss0: " + multiplication2("sssss0", "sss0"))

print("\nSubtraction:")
print("sssss0 - sss0: " + subtraction("sssss0", "sss0"))

print("\nSubtraction2:")
print("sssss0 - sss0: " + subtraction2("sssss0", "sss0"))

print("\nDivision:")
print("sssss0 / sss0: " + division("sssss0", "sss0") + ", Rest: " + subtraction("sssss0", multiplication("sss0", division("sssss0", "sss0"))))

print("\nDivision2:")
print("sssss0 / sss0: " + division2("sssss0", "sss0"))

print("\nModulo:")
print("sssss0 / sss0: " + modulo("sssss0", "sss0")) # 2
print("sssss0 / sssss0: " + modulo("sssss0", "sssss0")) # 0
print("sssss0 / ssssss0: " + modulo("sssss0", "ssssss0")) # sssss0
print("sssss0 / 0: " + modulo("sssss0", "0")) # NOT DEFINED!

# AUSGABE:
# Addition:
# sssss0 + sss0: ssssssss0 KORREKT
# Addition2:
# sssss0 + sss0: ssssssss0 KORREKT

# Multiplication:
# sssss0 * sss0: sssssssssssssss0 KORREKT

# Multiplication2:
# sssss0 * sss0: sssssssssssssss0 KORREKT

# Subtraction:
# sssss0 - sss0: ss0 KORREKT

# Subtraction2:
# sssss0 - sss0: ss0 KORREKT

# Division:
# sssss0 / sss0: s0, Rest: ss0 KORREKT 

# Division2:
# Traceback (most recent call last):
#   File "C:\Users\Hanno\Desktop\operatoren.py", line 132, in <module>
#     print("sssss0 / sss0: " + division2("sssss0", "sss0"))
#           ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "NoneType") to str