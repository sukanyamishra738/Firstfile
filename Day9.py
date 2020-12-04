# 1.Create a lambda function that multiplies argument x with argument y
product = lambda x,y : x * y
print(product(2,4))

# 2.Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0,1])
print(fib_series(5))

# 3.Write a Python program that multiply each number of given list with a given number
my_list = [1,2,3,4,5]
given_number = 3
new_list = list(map(lambda a: a*given_number,my_list))
print(new_list)

# 4.Write a Python program to find numbers divisible by 9 from a list of numbers
my_list1 = [2,3,9,15,18,20,27]
new_list1 = list(filter(lambda a: (a%9 == 0),my_list1))
print(new_list1)

# 5.Write a Python program to count the even numbers in a given list of integers
my_list2 = [1,2,3,4,5,6,7,8,9,10]
new_list2 = list(filter(lambda a: (a%2 == 0),my_list2))
print(new_list2)