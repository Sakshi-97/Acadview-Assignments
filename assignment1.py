# Q1: Print anything you want on screen.
print("Hello!I am new to PYTHON") #I simply write a statement to print it.

# Q2: Join two strings using '+' E.G. "Acad" + "View".
s1 =  "Sakshi" #I take first string.
s2 = "Arora" #another string.
print(s1+s2) #here, we are using '+' to join two sttings i.e. s1 & s2.

#Q3: Take the input of three variables x,y and z and print their values.
x = input("enter the value of first variable :") #it will take the value of x form the user.
y = input("enter the value of second variable :") #it will take the value of y from the user.
z = input("enter the value of third variable :") #it will take the value of z from the user.
print x,y,z #it simply prints all three values.

#Q4: Print "Lets get's started" on screen.
print("Lets get's started") #here we simply prints above statement.

#Q5: Print the following values using place holders s="Acadview" course="Python" fees=5000
print("The institution name is %s.\n The course name is %s.\n And the fees is %d.")%("Acadview","Python",5000)
#first place holder takes the value of instituion name ,second takes the course name and third takes the fees value respectively.

#Q6: let's do intresting exercise: name="Tony shark" salary=1000000 print(%s %d)%(____,____)
name="Tony Shark"
salary=1000000
print("name : %s\nsalary : %d")%(name,salary)