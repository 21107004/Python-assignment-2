#Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.#

number_1 = int(input("Enter 1st number "))

number_2 = int(input("Enter 1st number "))

ex_or = number_1 ^ number_2

bin_exor = bin(ex_or)
check_string = str(bin_exor)

a = check_string.count("1")

print(a)

print(check_string)
