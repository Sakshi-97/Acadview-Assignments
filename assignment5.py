# Q1: Create a function to find area of circle using user input of radius.
pi = 3.14 #pre define the value of pi.
def area_circle(): #a function is define named as area_circle.
    radius = float(input("Enter the radius of circle -- ")) #user enter the radius.
    area = pi*radius*radius #area is calculated.
    print("The area is %.2f" %area) #area will be printed.
area_circle() #calling of the function.

# Q2:
def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect(6))

# Q3: Print multiplication table of 12 using recursion.
num = 12 #number
def table(num, t=1): #a function hich returns the table of 12.
    if(t==11): #bcz we want multiplication till 10.
        pass
    else:
        print(num, 'x', t, '=', num * t)
        table(num, t+1) #increrment each time aafter multiply.
table(12) #calling of function.

# Q4: write a function to find power of a number raised to the other (a^b) using recursion.
x = int(input("Enter x -"))
y = int(input("Enter y -"))
def power(x, y): #a function which calculate the powers.
    if(y==1):
        return x #a number raised to the power 1 is number itself.
    elif(y==0):
        print(1) #a number raised to the power 0 is 1.
    if(y>1):
        z=x * power(x, y - 1) #power calculation.
        print(z)
power(x,y) #calling of function.

# Q5: Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def factorial(n): #a function which gives you a factorial.
    if(n <= 1): #if a number is 1 or less than 1 factorial is always 1.
        return 1
    else:
        return(n*factorial(n-1)) #calculate factorial.
n = int(input("Enter number:")) #enter number by user.
print("Factorial:")
print(factorial(n)) #print factorial.

