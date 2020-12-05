# 1.Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
list1 = ["AMIT","JAYA","HEERA"]
list2 = ["COGNIZANT","TCS","INFOSYS"]
a = list(tuple(zip(list1,list2)))
print(a)

# 2.First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
list3 = ["amit","jaya","sukanya","sweety","sidharth","krishna","connell","marianne"]
b = range(1,8)
merged = list(tuple(zip(list3,b)))
print(merged)

# 3.Using sorted() function, sort the list in ascending order.
list4 = ["audi","mercedes","skoda","aston martin","porsche"]
print(sorted(list4))

# 4.Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
list5 = [1,2,3,4,5,6,7,8,9,10]
odds = list(filter(lambda n : n%2!=0,list5))
print(odds)