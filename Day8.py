# 1)List down all the error types and check all the errors using a python program for all errors
# 1.NameError
try:
    print(hello)
except NameError as e:
    print("NameError",e)
# 2.IndexError
try:
    L = [1,2,3]
    print(L[3])
except IndexError as e:
    print("IndexError",e)
# 3.KeyError
hobby = {"sam":"dance","jam":"singing"}
try:
    print(hobby["tam"])
except KeyError as e:
    print("KeyError",e)
# 4.ImportError
try:
    from math import cube
except ImportError as e:
    print("ImportError",e)
# 5.TypeError
try:
    '2'+2
except TypeError as e:
    print("TypeError",e)
# 6.ValurError
try:
    int('sweety')
except ValueError as e:
    print("ValueError",e)
# 7.ZeroDivisionError
try:
    x = 1/0
except ZeroDivisionError as e:
    print("ZeroDivisionError",e)

# 2)Design a simple calculator app with try and except for all use cases
def Addition():
    try:
        c = int(input("enter first number:"))
        d = int(input("enter second number"))
        sum = c + d
        print("Here you go,", str(sum))
    except:
        print("Enter a valid integer")
def subtraction():
    try:
        c = int(input("enter first number:"))
        d = int(input("enter second number"))
        difference = c - d
        print("Here you go,", str(difference))
    except:
        print("Enter a valid integer")
def Multiplication():
    try:
        c = int(input("enter first number:"))
        d = int(input("enter second number"))
        multiplication = c * d
        print("Here you go,", str(multiplication))
    except:
        print("Enter a valid integer")

def Division():
    try:
        c = int(input("enter first number:"))
        d = int(input("enter second number"))
        division = c / d
        print("Here you go,", str(division))
    except:
        print("Enter a valid integer")

def code_calculator():
    print("Calculator:-")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    your_input = " "
    try:
        your_input = int(input("enter the arithmetic operation you want:"))
    except:
        print("enter a valid option")
    if(your_input == 1):
        Addition()
    elif(your_input == 2):
        subtraction()
    elif(your_input == 3):
        Multiplication()
    elif(your_input == 4):
        Division()
code_calculator()

# 3)print one message if the try block raises a NameError and another for other errors
try:
    print("hello")
    s = int(input("enter a number:"))
    print(s)
except NameError:
    print("it's a NameError")
except:
    print("other errors")
# 4)When try-except scenario is not required?

# 5)Try getting an input inside the try catch block
try:
    new_input = int(input("input number"))
except:
    print("Enter a valid input")


