# An annoying while loop
# name = ''
# while name != 'your name':
#     print('please type your name')
#     name = input()
# print('Thank you!')

# An annoying while loop (break)
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')

# import random, sys, os, math

# Guess the number game
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20')

# for guessesTaken in range (1, 7):
#     print('Take a guess')
#     guess = int(input())

#     if guess < secretNumber:
#         print('Your guess is too low')
#     elif guess > secretNumber:
#         print('Your guess is too high')
#     else:
#         break

# if guess == secretNumber:
#     print(f'Congratulations! You guessed the number in {guessesTaken} guesses!')
# else:
#     print(f'Unlucky.. I was thinking of {secretNumber}')

#Rock Paper Scissors game
# import random, sys

# print('ROCK, PAPER, Scissors')

#These variables keep track of the number of wins, losses and ties.
# wins = 0
# losses = 0
# ties = 0

# while True:                                                             #Main game loop
#     print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
#     while True:                                                         #Player input loop
#         print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit()                                                  #Quits the program
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#             break                                                       #Break out of move loop
#         print('Please type in your move')

    #Display what the player chose
#     if playerMove == 'r':
#         print('Rock versus...')
#     elif playerMove == 'p':
#         print('Paper versus...')
#     elif playerMove == 's':
#         print('Scissors versus...')

    #Display what the computer chose
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     if randomNumber == 3:
#         computerMove = 's'
#         print('SCISSOR')

    #Display and record the win/loss/tie record
#     if playerMove == computerMove:
#         print('Its a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1


# Q1:
# True and False

# Q2:
# and, or, not

# Q3:
# Nah fam

# Q4:
# False
# False
# True
# False
# False
# True

# Q5:
# !=
# ==
# >=
# <=
# >
# <

# Q6:
# Equal to compares two values. the assignment operator, assigns a value to a variables

# Q7:
# A condition is a value that is to be True or False in a loop

# Q8:
# Geen idee

# Q9:
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings!')

# Q10:
# ctrl + c

# Q11:
# Break, breaks out of the loop. Continue loops it back to the beginning.

# Q12:
# There is no difference

# Q13:
# i = 1
# for i in range(11):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i = i+1

# Q14:
# spam.bacon()