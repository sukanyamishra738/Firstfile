# 1)Write a program to loop through a list of numbers and add +2 to every value to elements in list
Numbers_list = [100 , 200 , 300 , 400 , 500]
for i in Numbers_list:
    print(i + 2)

# 2)Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1
for x in range(5,0,-1):
    for y in range(x,0,-1):
        print(y,end="")
    print("\n")

# 3)Python Program to Print the Fibonacci sequence
first = 0
second = 1
next = 0
Range = int(input("enter the range:"))
print(first,second,end=" ")
for i in range(2,Range):
    next = first + second
    print(next,end =" ")
    first = second
    second = next
print("\n")
# 4)Explain Armstrong number and write a code with a function
def check_an_armstrong_number():
    num = int(input("enter a number to check:"))
    temp = num
    sum = 0
    while num > 0:
        dig = num % 10
        sum = sum + (dig**3)
        num = num // 10
    if (temp == sum):
        print(str(temp) + " is an Armstrong number")
    else:
        print(str(temp) + " is not an Armstrong number")
check_an_armstrong_number()

# 5)Write a program to print the multiplication table of 9
def multiplication_table():
    print("Multiplication Table of 9:")
    for multiplier in range(1,11):
        result = 9*multiplier
        print(str(9) + "x" + str(multiplier) + "=" + str(result))
multiplication_table()

# 6)Check if a program is negative or positive
def check_if_positive_or_negative():
    given_number = int(input("enter a number:"))
    if given_number < 0:
        print("negative number")
    else:
        print("positive number")
check_if_positive_or_negative()
# 7)Write a program to convert the number of days to ages
def convert_days_into_years():
    days = int(input("enter the days:"))
    years = days//365
    print("the no.of years:" + str(years))
convert_days_into_years()

# 8)Solve Trigonometry problem using math function write a program to solve using math function
import math
def sine_function():
    a = int(input("enter a number for the sine function:"))
    print(math.sin(a))
def cosine_function():
    b =int(input("enter a number for the cosine function:"))
    print(math.cos(b))
sine_function()
cosine_function()

# 9)Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
def Addition():
    c = int(input("enter first number:"))
    d = int(input("enter second number"))
    sum = c + d
    print("Here you go,", str(sum))
def subtraction():
    c = int(input("enter first number:"))
    d = int(input("enter second number"))
    difference = c - d
    print("Here you go,", str(difference))
def Multiplication():
    c = int(input("enter first number:"))
    d = int(input("enter second number"))
    product = c * d
    print("Here you go,",str(product))
def Division():
    c = int(input("enter first number:"))
    d = int(input("enter second number"))
    quotient = c / d
    print("Here you go,", str(quotient))
def code_calculator():
    print("Calculator:-")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    operation = input("enter the arithmetic operation you want:")
    if(operation == "1"):
        Addition()
    elif(operation == "2"):
        Subtraction()
    elif(operation == "3"):
        Multiplication()
    elif(operation == "4"):
        Division()
code_calculator()


