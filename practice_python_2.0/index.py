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
# function import
 # import a specific function: from math import sqrt
 # import a universal function: from math import *
  # is not advisable import a ton of variables and functions
   # import math, example = dir (math), print example 
# max() min() abs() type()

#v1.4.1 Project Number Guess

# randint() from random import randint
# sleep() from time import sleep
# raw_input(), takes a string input convert to a integer
 # int(raw_input())

#v1.5.0 Lists and Dictionaries

#v1.5.1 Lists

# list is a datytype (strings, numbers, Booleans)
# list_name[index] starts with 0
# append() len() sort()
# list_name[:3] or [3:] or [4:6]
# insert() name.insert(1, "")
# index() name.index("")
# for variable in list_name
 # does the same thing for every list-item: for variable in list_name 
# remove item from list
 # list_variable.remove('value')

# v1.5.2 Dictionary

# dictionary a list using a key (instead of an index)
# great forloginpages, phonebooks
# variable = {'key' : value}, the value is a string / number 
# print (variable ['key'])    
# mutable
 # new: dictionary_variable ['new_key'] = 'value'
 # len() counts the number of key value pairs (output = integer)
 # delete: del dictionary_variable ['key'] = 'new_value'
 # reneame: dictionary_varaible['key'] = 'new_value'

#v1.5.3 Project a day at the supermarket

# FOR-loop
 # List 
  # for variable_loop in variable
  # print variable_loop
 # Dictionary
  # for variable_loop in variable_dictionary
  # print variable_dictionary[variable_loop]

#v1.5.4 Project Rock, Paper, Scissors

# raw_input() randint() 
# from random import randint

#v1.5.5 Project Student becomes the Teacher

# \ continuation character (of the current line)
# if elif else (= chain of statements)

#v1.6.1 List Accessing

# print variable []
# edit: n[1] = n[1] * 5
# append (): variable.append(element)
# remove
 # pop() removes index + returns
 # remove() removes item, not index
 # del(variable[]) removes item
# print item by item: 
""""
n = [3, 5, 7]
def list(x):
  for var_loop in range(0, len(x)):
    print x(var_loop)
print(list(n))
"""""
# modify each item
""""
n = [3, 5, 7]
def list(x):
  for var_loop in range(0, len(x)):
    x[i] = x[i] * 2
  return x
"""""
# range() generates a list of numbers

#v1.6.2 Project Battleship

# board = ['O', 'O', 'O', 'O', 'O']

print([0]*5)

board = []
for grid_range in range(5):
  board.append([0]*5)
#print(board)

def print_grid(grid_in):
  for row_grid in board:
    print(row_grid)
    # print" ".join(row_grid) // python 2.0

# randint()
# raw_input() asks user for a input, returns a string
# if else: break if: elif: else: if:

for i in range(0, 6):
  print(i)

# v1.7 Loops
 # often used for validation check for input
 # types
  # for-each iterate trough list/dictionary, doesn't give an index
  # for gives an index, gives position
  # while when not sure to use a loop
  # while-else and for-else gives functionalilty when loops exits normally


# v1.7.1 While

# while keeps executing while its true, stop with:
 # increment +1
 # condition
 # break, exits the current loop
# otherwise it becomes an infinite loop which never exits

# while/else
 # when loop-conditon is false, the code-block in else always executes

# v1.7.2 For
 # iterate trough a list
 # iterate trough a dictionary

# enumerate() counts the index within a list
# zip() iterate trough multiple lists