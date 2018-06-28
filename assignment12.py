# Q.1- Name and handle the exception occured in the following program:
a=3
try:
    if a<4:
       a=a/(a-3)
       print(a)
except ZeroDivisionError:
    print("Error Occured! as divison by zero is not possible.")
finally:
    print("The value of a is :",a)

# Q.2- Name and handle the exception occurred in the following program:
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Error Occured! Index 3 is not in the list")

#Q.3- What will be the output of the following code:
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print "An exception"
#     raise  # To determine whether the exception was raised or not
#The output will be:
#An exception
#NameError: Hi there

#Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#the output will be:
#-5.0
#a/b result in 0

#Q.5- Write a program to show and handle following exceptions:
#1. Import Error
try:
    import cv
except ImportError:
    print("There is no module named as 'cv' to import.")
#2. Value Error
try:
     a = int(input("Enter a positive integer: "))
     if a <= 0:
         raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
#3. Index Error
lst = ['sakshi',25,'python']
try:
    print (lst[5])
except IndexError:
    print("Erorr index!")

#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).
try:
    age = int(input("Enter your age: "))
    if(age<18):
        pass
    raise AgeTooSmallError("You are too small to acess Python!")
except AgeTooSmallError:
    new_age = int(input("Enter your age again: "))
    raise
