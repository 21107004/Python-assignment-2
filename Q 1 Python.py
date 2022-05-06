#For a given input string “Python is a case sensitive language”. Write pythoncode for the following#
a = input("Python is a case sensitive language")
#Find the length of the input string#
b = len(a)

print("Length of the string is:\n",b)
#Reverse the order of the string in one line code.#
c = a[::-1]
print("The reversed string is:\n",c)
#Using Slice function store “a case sensitive” in new string.#
d = a[10:26]

#Replace “a case sensitive” with “object oriented”.#
a_1 = a.replace("a case sensitive", "object oriented")

print(a_1)

#Find index of substring “a” in the given input string.#

f = a.find("a")
print('Index of "a" substring in input string is:',f)

#Remove the white spaces from the given input string.#
g = a_1.replace(" ", "")

print(g)



