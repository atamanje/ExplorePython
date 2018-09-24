#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:02:17 2018

@author: jessieatamanchuk
"""

# This program will explore the properties and behavior of classes, methods,
# functions, conditional statements, loops, tuples and boolean operation




## Functions
# A function may be defined using the 'def' keyword
# To begin the function we use a colon. Notice there are no limiters like 'end'
# or curly braces used. Python uses the amount of indentation to limit 
# functions, classes, methods, if statements and loops.

# Example of defining a function without arguments
def func1():
    print('Hello World!')

# A function will be executed when the name is called with parentheses and all
# needed arguments    
    
# Example of calling a function
print('A function with no arguments:')
func1()

# If arguments are needed for the function to operate, these are added into the
# parentheses, arguments may be of any data type and may not even be limited
# '*args'. If '*args' is used, it must be the last argument entry. If arguments
# are supplied where none are needed, the function doesn't use them

# Example of defininf a function with arguments
def func2(x,y):
    area = x*y
    print('The area of a rectangle with sides '+str(x)+' and '+str(y)+\
          ' is '+str(area)+'.')
    
# Example of calling a function with arguments
print('\nA function with arguments:')
func2(3,4)

# Example of deining a function with unlimited arguments
def func3(*args):
    print(args)
    
# Example of calling a function with unlimited arguments
print('\nA function with unlimited arguments:')
func3(1,2,3,4,5,6,7,8,9)
print('\nThe same function:')
func3('abc','DEF','ghi')

# The final thing to note about functions is that the arguments do not need to
# be defined in the call statement as they are defined sequentially in the def
# statement

# Example of calling a function with non-sequential arguments
print('\nA function with criss-crossed arguments (func2):')
func2(y=4,x=3)




## Classes & Methods
# A class is a template definition of the methods and variables in a 
# particular kind of object . Thus, an object is a specific instance of a 
# class; it contains real values instead of variables
#
# A class may be defined using the 'class' keyword. We then enter the name of 
# the class and parentheses. As with functions, we then initialise a class 
# using a colon and proper indentation. After a class is defined, we mayadd 
# methods and variables.
#
# To speak about variables for a moment, there are two types when it comes to
# classes. These are class and instance variables. Class variables are shared 
# by all instances of the class through objects, class variables are defined
# before methods are defined. Instance variables are variables are not shared 
# by all instances of the class and are therfore defined by the object. Thus, 
# it is only logical that instance variables be defined by the object in the 
# methods of the class. 
#
# A method is a function inside a class.

# Example of a class with no methods
print('\nA class with no methods initialising:')
class class1():
    print('Nothing in here... :/\n')

# Example of creating an object with class1
print('\nA class with no methods:')
obj1 = class1()
print(obj1)

# ^^ NOTE that the class1 is ran as soon as it is defined and also that obj is 
# equal to the string definition of class1 because of a lack of output

# Example of a class with methods
class class2():
    def meth1(self):
        print('Class 2, Method 1')
    def meth2(self):
        print('Class 2, Method 2')

# Example of craeting a object wth class2
print('\nA class with methods (no arguments):')
obj2 = class2()
obj2.meth1()
obj2.meth2()

# Example of a class with class variables
class class3():
    var1 = 'Python is cool'
    
# Example of calling a class with class variable
print('\nA class with class variables:')
print('One object:')
obj3a = class3()
print(obj3a.var1)
obj3b = class3()
print('Another object:')
print(obj3b.var1)

# Example of class with instance variables
class class4():
    def meth1(self,x,y,z):
        self.instVol = x*y*z
        print('The volume of a prism with sides '+str(x)+', '+str(y)+\
              ', '+str(z)+' is '+str(obj4.instVol)+'.')
        

# Example of calling a class with a method that uses instance variables
print('\nA class with instance variables:')
obj4 = class4()
obj4.meth1(3,4,5)
print('This is the volume outisde the class, volume = '+str(obj4.instVol)+'.')




## Conditional Statements
# A conditional statement in many programming language consists of 3 different
# statements: if, elseif and else

# Example of an if statement
print('\nAn if satement:')
x = 3
y = 4
if x < y:
    print('x is less than y')

# Example of an elseif statement
print('\nAn if-else satement:')
x = 4
y = 3
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
    
# Example of an else statement
print('\nAn else satement:')
x = 3
y = 3
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y:')
 
    
    
    
## Boolean operations
# A boolean statement in programming languages is a comparison statement 
# between two values. The result of a boolean statement is 0 or 1, true or 
# false, respectively. Boolean values are needed for a wide range of objectives
# in coding, most previlently, they are used in conditional statements
    
# Example of the 'less than' operation
print('\nIs 4 less than 3')
x = (4 < 3)
print(x)

#Example of the 'less than equal to' statement
print('\nIS 4 less than equal to 3:')
x = (4 <= 3)
print(x)

#Example of the 'greater than' statement
print('\nIs 4 greater than 3:')
x = (4 > 3)
print(x)

# Example of the 'greater than equal to' statement
print('\nIs 4 greater or equal to 3:')
x = (4 >= 3)
print(x)

# Example of the 'equal to' statement
print('\nIs 4 equal to 3:')
x = (4 == 3)
print(x)

# Example of the 'not equal to' statement
print('\nIs 4 not equal to 3:')
x = (4 != 3)
print(x)

# Example of the 'and' statements
x = [3,4]
print('\nAre 3 or 4 less than 3.5:')
y = ((x[0] and x[1]) < 5)
print(y)
    
# Example of an 'or' statement
print('\nAre 3 or 4 greater than 3.5:')
y = ((x[0] or x[1]) > 3.5)
print(y)
    
# Example of an 'in' statement
print('\nIs 6 in the array [3 4]:')
y = (6 in x)
print(y)

# Example of an 'is' statement
print('\n"Is" ''abc'' equal to ''def'':')
y = ('abc' is 'def')
print(y)

# Example of a 'not/is' statement
print('\n"Is" ''abc'' "not" equal to ''def'':')
y = ('abc' is not 'def')
print(y)

# Example of an 'in' statement
print('\nIs 3 "in" the array [3 4]:')
y = (3 in x)
print(y)

# Example of a 'not/in' statement
print('\nIs 3 "not in" the array [3 4]:')
y = (3 not in x)
print(y)




## Tuples
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just
# like lists. The differences between tuples and lists are, the tuples cannot 
# be changed unlike lists and tuples use parentheses, whereas lists use square 
# brackets. Although a tuple's values may not be altered, tuples may be joined 
# together to create new tuples. Boolean operations may also be performed on 
# tuples.

# Example of defining a tuple. As said earlier a tuple if defined by using 
# parentheses, whereas hard brackets are used to define an array.
tup1 = (1,2,3)
print('\nDefining and calling a tuple:')
print(tup1)

# Example showing the inability to change tuple properties
print('\nOne may not change tuple properties:')
print('TypeError: "tuple" object does not support item assignment')

# Example of how tuples may be made of a mix of data inputs
print('\nTuples can consists of different data types:')
tup2 = ('abc','def','ghi')
tup3 = (1,2,3,'abc','def','ghi')
print(tup1)
print(tup2)
print(tup3)

# Example of an empty tuple
tup4 = ()
print('\nTuple may be empty:')
print(tup4)

# Example of indexing a tuple
print('\nA tuple may be indexed like a regular array:')
print('tup3[0,2,4,6] =',tup3[0],',',tup3[2],',',tup3[4],'.')

# Example of tuple concatanation
print('\nTuple can be joined together into a new tuple:')
tup5 = tup3 + tup1
print(tup5)

# Example of deleting a tuple
print('\nA tuple may be deleted:')
del(tup5)
print('NameError: name "tup1" is not defined')


# Example of tuple functions, length
print('\nThe length of a tuple can be found:')
print(len(tup3))

# Example of repetitive tuple creation
print('\nA repetitive tuple can be created:')
tup6 = ('tup',)*8
print(tup6)

# Example of comparing tuples
#print('\nTuple may be compared. Is tup2 equal to tup4: ')
#bool1 = cmp(tup2,tup4)
#print(bool1)

# Example of getting the max tuple value
print('\nThe maximum tuple index can be gotten:')
val = max(tup1)
print(val)

# Example of getting the min tuple value
print('\nThe minumum tuple index can be gotten:')
val = min(tup1)
print(val)

# Example of creating a tuple from an array
print('\nCreate a tuple from a list:')
tup7 = tuple([1,2,3] + [5,6,7])
print(tup7)