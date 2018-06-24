# Q.1- Take 10 integers from user and print it on screen.
for i in range(10): # a loop which takes 10 inputs.
    num = int(input("Enter any integer:")) #user enters integers.
   print("you entered integer is :", num) #simantaneously prints the value user enters.

# Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while True: #the condition here for the while loop is always true.
   print("INFINITE!") #so the loop is run infinity times.

# Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
#for i in range(3):
  #  numbers = int(input("Enter any integer:"))
 #   list_1 = numbers
#print("you enterred numbers are:",list_1)

# Q.5- Using range(1,101), make a list containing even and odd numbers.
for x in range(1,101): #a particular range given
    print(x) #prints the number.
    if(x%2==0): #condition for checking that a number is even or odd.
        print("The number is an even number.")
    else:
        print("The number is an odd number.")

# Q.6- Print the following patterns:
# *
# **
# ***
# ****
print("Here's the following patter you want--")
for x in range(5): #range according the pattern is set.
    print("*"*x)

# Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.
dict_a = dict() #declare a dictionary.
for j in range(3): #set a range.
    key = input("Enter key: ") #user enter key.
    value = input("Enter value: ") #user enters value.
    dict_a[key] = value
print(dict_a)# prints the dictonary.

# Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
i = ['a','b','c','d','b'] #a list having some elements
i_count = 0
for z in i:
    if(z=='b'): #condition to check whether the element is in the list or not.
        i.remove(z) #if true then delete it.
print(i)