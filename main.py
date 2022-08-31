#Functions 
'''A function is a block of code which only runs when it is called. You can pass data , known as parameter, into a function. A function can gte data as a result.'''
#Creating a function
#In python a function is created using the def keyword
'''def my_function ():
  print ("Hello from a function")

#Calling a Function
#To call a function, use the function name followed by parentheses'''
def my_function ():
  print ("Hello from a function") 
my_function()
#Example
def my_function (fname):
  print (fname + " Joaquin")
my_function ("Pizza")
#Parameters or Arguments
#The terms parameter and argument can be used for the same thing : information that are passed into a function/executed into a function
#A parameter is the variable listed inside the parentheses in the function definition
#An argument is the value that is sent to the function when it is called
def my_function (fname, lname):
  print (fname + " " + lname)
my_function("Carlos", "Campuzano")

# Python Class
# To create a class use key word class
# Create a class name MyClass with a property named x
class MyClass:
  x = 5

# Create an object
# We can use the class name MyClass to create an object
#Create an object named g1 and print the value of x
p1 = MyClass()
print (p1.x)
# The_init_() Function
# Use the_init_() Function to assign values for name and age
# Example create a class named Person. Use the_init_() Function to assign values for name and age
class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age
p1 + Person ("John" , 36)
print (p1.name)
print (p1.age)
# Note the_init_() Function is called automatically every time the class is being used to create a new function
# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class they inherited from. Also called base class.
# Child class is the class that inherits from another class. Also called derived class. 
# Any class can be parent, so syntax is the same as creating other class
# Example Create a class named Person with first name and last name properties and a printname method
class Person: # Parent class
  def _init_ (self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname (self):
    print (self.firstname, self.lastname)
# Use Person class to create an object, and then execute the printname method
x = Person ("John", "Doe")
x.printname()
# Child Class
# To create a class that inherits the functionality from another class send the parent class as a parameter when creating the child class. 
# Example Assignment Create a class named Student which will inherit the properties and methods from the Person class.
class Student(Person):
  pass
# Ex: Use the student class to create an object and then execute the printname method
x = Student ("Mike", "Olsen")
x.printname()