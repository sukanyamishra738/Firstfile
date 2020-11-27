# 1)Create a function getting two integer inputs from user. & print the following:
def Numbers():
    num1 = int(input("first number:"))
    num2 = int(input("second number:"))
# Addition of two numbers is +value
    sum = num1 + num2
    print("Addition of " + str(num1) + " and " + str(num2) + " =", sum)
# Subtraction of two numbers is +value
    difference = num1 - num2
    print("Difference of " + str(num1) + " and " + str(num2) + " =", difference)
# Division of two numbers is +value
    division = num1 / num2
    print("Division of " + str(num1) + " and " + str(num2) + " =", division)
# Multiplication of two numbers is +value
# Here the value represents math function associated
    multiplication = num1 * num2
    print("Multiplication of " + str(num1) + " and " + str(num2) + " =", multiplication)
Numbers()
# 2)Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
def covid(Body_temp = 98):
    patient_name = input("Enter the patient name:")
    print("patient_name:",patient_name)
    print("patient's body temperature",Body_temp)
covid()


