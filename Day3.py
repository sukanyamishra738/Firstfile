# 1.Write a Python script to merge two Python dictionaries
Best_Enlist_registered_students = {"python":"50" , "react_js":"20" , "ML":"30" , "node_js":25}
newly_added ={"python":"65" , "Big_data":"18" , "Blockchain":"15"}
Best_Enlist_registered_students.update(newly_added)
print(Best_Enlist_registered_students)
# 2.Write a Python program to remove a key from a dictionary
Best_Enlist_registered_students.pop("node_js")
print(Best_Enlist_registered_students)
# 3.Write a Python program to map two lists into a dictionary
list1 = ["Ram","Shyam","Gita"]
list2 = ["Black","orange","Green"]
fav_color = dict(zip(list1,list2))
print(fav_color)
# 4.Write a Python program to find the length of a set
Fruits = {"apple","orange","mango","pear"}
print(len(Fruits))
# 5.Write a Python program to remove the intersection of a 2nd set from the 1st set
More_Fruits = {"guava","pineapple","custard apple","pear"}
Fruits.difference_update(More_Fruits)
print(Fruits)