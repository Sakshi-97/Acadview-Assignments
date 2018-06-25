#Q.1- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    legs = 4
    eyes = 2
    name = 'Animal'
    def animal_attibute(self):
        print(self.name+" can walks with %d legs"%self.legs)
        print(self.name+" can see with %d eyes"%self.eyes)

class Tiger(Animal):
    name = 'Tiger'

a1 = Animal()
a1.animal_attibute()
t1 = Tiger()
t1.animal_attibute()

#Q.2- What will be the output of following code.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g() #the output of this code will be: A B \n A B

#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details. Create another class Mission which extends the class Cop.
# Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a
# particular cop and make it available for mission.
class Cop:
    def __init__(self):
        self.name = "Sakshi"
        self.age = 26
        self.work_exp = "6 years"
        self.designation = "DSP"

    def display(self):
        print("The name of the cop is: ",self.name)
        print("The age of the cop is: ", self.age)
        print("The work experience of the cop is: ", self.work_exp)
        print("The designation of the cop is: ", self.designation)

    def update(self):
        self.name = "Manik"
        self.age = 29

class Mission(Cop):
    def  add_mission(self):
        print("The new cop is: ",self.name)
        print("The age of new cop is: ",self.age)
        self.mission_name = "Mission Python"
        self.location = "Acadview"
        print("The mission for the cop is: ",self.mission_name)
        print("The location for the mission is: ",self.location)


c1 = Cop()
c1.display()
m1 = Mission()
m1.update()
m1.add_mission()

#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.
class Shape:
    def __init__(self):

        self.length = int(input("Enter the value of the length: "))
        self.breadth = int(input("Enter the value of the breadth: "))

    def Area(self):
        if(self.length==self.breadth):
            print("The area of square is: ",self.length*self.length)
        else:
            print("The area od rectangle is: ",self.length*self.breadth)

class rectangle(Shape):
        print("this is the recatangle class")

class square(Shape):
        print("this is a square class")

r = rectangle()
r.Area()
