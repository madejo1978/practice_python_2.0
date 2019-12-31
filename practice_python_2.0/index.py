#v1.0 Syntax

# string
print ("Hello, world!")
print ("Hello, " + "Martin")

# error-handling
# variables
# arithmetic 
# updating varables -= +=
# comments
# integers: integers, float 
 # float() or .
# multi-line Strings """" """
# Booleans 
 # true false
# valueError convert dataTypes
 # str() int() float()

 #v1.1 Strings

 # escaping characters
 # access by index
 # methods
  # len() lower() upper() str()
  # call with a dot: variable.method() only with strings
# visual code is the editor, print() is the console output
# printing variables
# concatenate 
 # combining strings
print("Spam " + "and " + "eggs")
 # %-operater replaces the %s-parameters, use %02d-if variabele is an integer
g = "Golf"
h = "Hotel"
print("%s, %s" % (g, h))

#v1.2 Date and Time

# library import: from datetime import datetime
# datetime.now()
# extracting / formatting
from datetime import datetime
now = datetime.now()
print("%02d/%02d/%04d" % (now.month, now.day, now.year))

#v1.3 Conditionals & Control Flow

# comparators == != < <= > >=
# 3 boolean operators 
 # and, or, not
 # order without parentheses(): not, and, or 
# conditonal statements: executes when true
 # if: else: elif:
 # common errors: IndentationError, ParseError ^
 # use colons after every statement
# example
 # def function() if: elif: else: fuction()

#v1.3.1 Project PygLatin

# raw_input() len() isalpha() lower()
# variable[1:4] or variable[1:len(variable)]

#v1.3.2 Project AreaCalculator

# multi-line comment """ """
# raw_input() 
# exponentitation: radius**2 
# float-formatting %f % (variable)

#v1.4 Functions

# 3 compenents 
 # header, def name parameters
 # optional comment, explains what the function does
 # the body, describes procedure te function carries out
# call a function
# function(parameter, parameter, etc.). defining a function placeholder variables: parameters
 # function(arguments, arguments, etc.) calling a function inputs into a function: arguments
# generic import. import a module
 # import math => math.sqrt()
