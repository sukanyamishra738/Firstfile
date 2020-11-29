# 1)Create a python module with list and import the module in another .py file and change the value in list
import Day7
Day7.list1.append("Lata")
print(Day7.list1)
# 2)Install pandas package (try to import the package in a python file)
# pip install pandas
import pandas as pd
# 3)Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
import random
print(random.randint(1,100))
# 4)Import sys package and find the python path
import os
import sys
Pythonpath = os.path.dirname(sys.executable)
print(Pythonpath)

# 5)Try to install a package and uninstall a package using pip
# pip install flask
# pip uninstall flask