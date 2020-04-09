# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')

# def b():
#     print('b() starts')
#     c()
#     print('b() returns')

# def c():
#     print('c() starts')
#     print('c() returns')

# def d():
#     print('d() starts')
#     print('d() returns')

# a()

# def spam():
#     eggs = 99
#     eggs = bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0
#     return eggs

# spam()

# def spam():
#     eggs = 'spam local'
#     print(eggs)

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)

# eggs = 'global'
# bacon()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'

# def bacon():
#     eggs = 'bacon'

# def ham():
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)

# import time, sys

# indent = 0                                                                                      # How many spaces to indent
# indentIncreasing = True                                                                         # Whether the indentation is increasing or not

# try:
#     while True:                                                                                 # Main program loop
#         print(' ' * indent, end='')
#         print('*********')
#         time.sleep(0.1)                                                                         # Pause for 1/10th a second

#         if indentIncreasing:
#             indent = indent + 1                                                                 # Increases the indent
#             if indent == 20:
#               indentIncreasing = False                                                          # Change direction

#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indentIncreasing = True

# except KeyboardInterrupt:
#     sys.exit()

# Q1:
# They save reduntant code by reusing old code

# Q2:
# When it is called

# Q3:
# def function():

# Q4:
# A function call, calls the actual function. Only then will it run.

# Q5:
# one global scope, and one local scope

# Q6:
# If they are returned by the function. The variables are passed through

# Q7:
# A return value is a local variable that gets returned by a function

# Q8:
# None

# Q9:
# global variable

# Q10:
# NoneType

# Q11:
# It imports the functions from areallyourpetsnamederic

# Q12:
# spam.bacon()

# Q13:
# By defining except handlers

# Q14:
# In the try clause you test your code for errors. Within the try clause you can handle exceptions via the except clause.