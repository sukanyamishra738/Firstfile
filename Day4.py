# 1.Write a program to create a list of n integer values and do the following
amount = ["100" , "200" , "300" , "400" , "500"]
print(amount)
# •	Add an item in to the list (using function)
amount.append("600")
print(amount)
# •	Delete (using function)
amount.remove("100")
print(amount)
# •	Store the largest number from the list to a variable
largest = max(amount)
print("The largest number:", largest)
# •	Store the Smallest number from the list to a variable
smallest = min(amount)
print("The smallest number:", smallest)
# 2.Create a tuple and print the reverse of the created tuple
cars = ("audi","skoda","BMW")
rev = reversed(cars)
print(tuple(rev))
# 3.Create a tuple and convert tuple into list
print(list(cars))