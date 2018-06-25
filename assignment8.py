# Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
global radius #a variable radius is globally declared.
radius = int(input("Enter the radius of the circle: ")) #user enters the value of radius.
class circle: # a class circle ehich calculate the area and circumference.
    def getArea(self): #a method which calculates the area.
        area = 3.14*radius**2
        print "The area is :",area
    def getCircumference(self): #another method which calculates the circumference.
         cf = 2*3.14*radius
         print "The circumference is :",cf
c1 = circle() #an object is created.
c1.getArea() #caliing of the function.
c1.getCircumference()

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
    def info(self):
        print("Name of the student is:",self.name)
        print("Age of the student is:",self.age)
s1 = Student()
s1.info()

# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temprature:
    temp=0
    def convertFahrenheit(self):
        temp = int(input("Enter the temprature in celsius: "))
        temp = temp+32
        print("The temprature in faranhiet is :",temp)
    def convertCelsius(self):
        temp = int(input("Enter the temprature in faranheit: "))
        temp = temp-32
        print("The temprature in celsius is :", temp)
t1 = Temprature()
t1.convertFahrenheit()
t1.convertCelsius()

#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.
class MovieDetails:
    def __init__(self):
        self.movie_name = input("Enter the name of the movie: ")
        self.movie_artist = input("Enter the name of the artist: ")
        self.release_year = input("Enter the year of release: ")
        self.ratings = input("Enter the ratings of the movie: ")

    def Display(self):
        print("The name of the movie is: ",self.movie_name)
        print("The name of the artist is: ", self.movie_artist)
        print("The year of release is: ", self.release_year)
        print("The ratings of the movie is: ", self.ratings)

    def Update(self):
        self.new_movie = input("The name of new movie is: ")
        self.new_artist = input("The name of new artist is: ")
        self.new_release = input("The year of new release date is: ")
        self.new_artist = input("The new ratings is: ")

m1 = MovieDetails()
m1.Display()
m1.Update()

#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary
class Expenditure:
    def __init__(self):
        self.expenditure = input("Total expenditure of the month is: ")
        self.savings = input("Total savings of the month is: ")

    def display(self):
        print("Total expenditure of the month is : ",self.expenditure)
        print("Total savings of the month is : ",self.savings)

    def salary(self):
        self.total_salary = self.expenditure+self.savings

    def DisplaySalary(self):
        print("Total salary of the month is: ",self.total_salary)

e1 = Expenditure()
e1.display()
e1.salary()
e1.DisplaySalary()
