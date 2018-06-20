# Q1: Take an input year from the user and dicide whether it is a leap year or not.
year = input("Enter Year : ") #user enter the year.
if (year%4==0): #here the condition is checked that whether the year is divisible by 4 or not.
    print("The year is a leap year!") #if yes, then it is  aleap year.
else:
       print("The year is not a leap year!") #if not, then it is not a leap year.

# Q2: take length and breadth input from user and check whether the dimensions are of sqaure or rectangle.
first_side = input("Enter first side : ")
second_side = input("Enter second side : ") #user enters alll four sides.
third_side = input("Enter third side : ")
fourth_side = input("Enter fourth side : ")
if (first_side==third_side and second_side==fourth_side): #checks the condition of being rectangle.
    print("It is a RECTANGLE!")
elif (first_side==second_side and third_side==fourth_side):  #checks the condition of being square.
    print("It is a SQUARE!")
else:
    print("It is a shape other then square and rectangle!") #runs when both above condition is false.

 # Q3: Take the input age of 3 people  and determine thw oldest and the youngest one among them.
AVNEET=int(input("Enter age of Avneet")) #takes user input first.
SAKSHI=int(input("Enter age of Sakshi"))
MANIK=int(input("Enter age of Manik"))
if (AVNEET>SAKSHI and AVNEET>MANIK): #checks conditions.
    print("AVNEET is the oldest.")
    if(SAKSHI>MANIK):
        print("MANIK is the youngest.")
    else:
       print("SAKSHI is the youngest.")
elif (SAKSHI>AVNEET and SAKSHI>MANIK):
    print("SAKSHI is the oldest.")
    if(AVNEET>MANIK):
        print("MANIK is the youngest.")
    else:
        print("AVNEET is the youngest.")

else:
    print("MANIK is the oldest.")
    if (AVNEET>SAKSHI):
        print("SAKSHI is the youngest.")
    else:
        print("AVNEET is the youngest.") #using if else we get the desired output.

 # Q4:
SCORE=int(input("Enter score")) #user enters desired score.
if (181<=SCORE<=200): #condition checks.
    print("Congratulations! You won Choclates.") #prize declare according to the scorwe.
elif (151<=SCORE<=180):
    print("Congratulations! You won Book.")
elif (51<=SCORE<=150):
    print("Congratulations! You won Wooden Dog.")
else:
    print("Sorry! No prize this time.")
