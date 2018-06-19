# Q1: Create a list with user defined inputs.
l1 = [input('enter the elements:')] #input function takes the elements of list from the user
print l1 #the list is printed here.

# Q2: Append the following list in the above created list:
#  ["google","apple","facebook","microsoft","tesla"
l1.append("google") #append function adds these elements in the previious list in the end of the list.
l1.append("apple")
l1.append("facebook")
l1.append("microsoft")
l1.append("tesla")
print l1 #new updated list will print.

# Q3: Count the number of time an object occurs in the list.
l2 = [1,2,3,5,2,4,1,3,6,4,1,2,5,3,5,4] #a list is created having many numbers.
print l2.count(1) #count function returns you an int value of how many times an object occurs in a list.

# Q4: Create a list with numbers and sort it in ascending order.
l3 = [25,14,85,36,12,75,60] #a list is created with some numbers.
l3.sort() #sort function sort all the numbers.
print l3 #print new updated list

# Q5: Given are two one dimensional arrays A and B which are sorted in ascending order. write a  program to merge into a single sorted
#array C which contain every elements of A and B

A = [54,63,12,40] #
A.sort() #first sorted aaray.
print A
B = [78,36,15,23]
B.sort() #second sorted aaray.
print B
C = A+B #joininf of both arrays.
C.sort() #sorting of third array
print C