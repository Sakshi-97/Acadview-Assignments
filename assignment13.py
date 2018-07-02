# Q.1- Write a Python program to read last n lines of a file.
f = open("main.txt",'r')
last = f.readlines()
f.close()
n = input("enter no. of lines")
while n>0:
    print(last[n])
    c=-1

#Q.2- Write a Python program to count the frequency of words in a file.



#Q.3- Write a Python program to copy the contents of a file to another file
with open ( "p1.txt" ) as f:
with open ( "p2.txt" , "w" ) as f1:
for line in f:
f1. write( line

# Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
with open ( “p1.txt” ) as fh1 , open ( “p2.txt” ) as fh2 :
for line1 , line2 in zip ( fh1 , fh2 ):
print ( line1 + line2 )

#Q.5- Write a Python program to write 10 random numbers into a file.
#  Read the file and then sort the numbers and then store it to another file.
import random
with open("random.txt", "w") as f:
for i in range(int(input('How many random numbers? '))):
line = str(random.randint(1, 100))
f.writelines(line + '\n')
print(line)
with open("random.txt") as f1 ,open("random1.txt", "w") as f2:
lines = f1.read().splitlines()
lines.sort()
for l in lines:
f2.write(str(l) + '\n