# 1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
str = "@@@@Sukanya123@@@@"
matched = re.findall("[\w]", str)
for i in matched:
    print(i,end = " ")

print("\n")
# 2.Write a Python program that matches a word containing 'ab'.
import re
str1 = "fabulous,cab,dab"
matched1 = re.findall("ab",str1)
for x in matched1:
    print(x,end =" ")

print("\n")
# 3.Write a Python program to check for a number at the end of a word/sentence.
import re
str2 = "sukanya1,amit2,jaya3,raju"
matched2 = re.findall("[a-z]\d", str2)
for y in matched2:
    print(y,end = " ")

print("\n")
# 4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re
str3 = "sukanya738@"
for z in re.finditer("\d{1,3}",str3):
    loctup = z.span()
    print(str3,loctup,end = "")

print("\n")
# 5.Write a Python program to match a string that contains only uppercase letters
import re
str4 = "AMIT,JAYA,sukanya,sweety"

matched3 = re.findall("[A-Z]*", str4)
for w in matched3:
    print(w,end = " ")




