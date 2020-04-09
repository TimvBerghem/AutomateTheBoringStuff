################ Dog shelter Application #################

# dogList = []

# def addDog():
#     global dogList
#     addMore = 'Yes'

#     while addMore == 'Yes' or addMore == 'yes':
#         print('\nPlease enter the name of your dog:')
#         dogList = dogList + [str(input())]

#         print(f'\n{dogList[-1]} will be taken good care off! \n')
#         print('\nDo you wish to add more dogs? Yes or No:')
#         addMore = str(input())

# def depositDog():
#     global dogList
#     pickMore = 'Yes'

#     while pickMore == 'Yes' or pickMore == 'yes':
#         print('\nPlease enter the name of the dog you want to pick up:')
#         dogPickup = str(input())
#         print(f'{dogPickup} has been eagerly awaiting your return. Look at how happy he is!')
#         dogList.remove(dogPickup)

#         print('\nThe following dogs are still at our shelter:')
#         for dogs in dogList:
#             print(dogs)

#         print('\nWould you like to pick up another dog?')
#         pickMore = str(input())

# def showDogList():
#     print(f'\nWe have {len(dogList)} of your dogs in our shelter. \nThe following dogs have been administered:')
#     dogList.sort(key=str.lower)

#     for dogs in dogList:
#         print(f'- {dogs}')

# def dogAdministration():                                                #Main program loop
#     print('Welcome to the dog shelter')

#     while True:
#         print('Do you want to add your dog, or pick him up? (add, pickup or none)')
#         userInput = str(input())

#         if userInput == 'add':
#             addDog()                                                        #Lets user add dogs
#         elif userInput == 'pickup':
#             depositDog()
#         else:
#             break

#     showDogList()                                                       #Displays dogs left at shelter

# dogAdministration()                                                     #Run program

##############################################################################################################################


# def eggs(someParameter):
#     someParameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

##############################################################################################################################

# import copy
# spam = ['A','B','C','D']
# print(id(spam))

# cheese = copy.copy(spam)
# print(id(cheese))

##############################################################################################################################


############ Conway's game of life ############


# import random, time, copy
# WIDTH = 60
# HEIGHT = 20

#Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.

# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)

#    Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # Print the # or space.
#         print() # Print a newline at the end of the row.

#    Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#            Get neighboring coordinates:
#            `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord  = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT

#            Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.

#             Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or
# numNeighbors == 3):
#                Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(0.25) # Add a 1-second pause to reduce flickering.


##############################################################################################################################


# Q1:
#     Creates a list

# Q2:
#     spam[2] = 'Hello'

# Q3:


# Q4:
#     D

# Q5:
#     A, B

# Q6:
#     1

# Q7:
#     3.14, cat, 11, cat, True, 99

# Q8:
#     3.14, 11, cat, True, 99

# Q9:
#     + and *

# Q10:
#     append puts its value at the end of the list. With insert you place the value within the list.

# Q11:
#     bacon.remove()
#     del statement

# Q12:
#     Can be indexed
#     Can be concantenated, multiplied etc.

# Q13:
#     Lists are mutable, tuples are immutable.
#     References to lists are referencing the same list ID,
#     References to tuples create completely new IDs

# Q14:
#     spam(42,)

# Q15:
#     the tuple() and list() variables

# Q16:
#     They contain references to the lists

# Q17:
#     copy, copys the top layer of the list.
#     deepcoyp, copys all the layers of the lists


###########################################################################################################################


########### Comma code ############

# spam = ['apples', 'bananas', 'tofu', 'cats']

# def comma(lijst):
#     for word in lijst:
#         print(f'{word}, ', end = '')


########### Picture Grid ###########

# grid = [['.', '.', 'O', 'O', '.', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
#         ['.', '.', 'O', 'O', 'O', 'O', 'O', '.', '.'],
#         ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', 'O', '.', '.', '.', '.']]


# for x in range(len(grid)):
#     for y in range(len(grid[0])):
#         print(grid[x][y], end='')
#     print()