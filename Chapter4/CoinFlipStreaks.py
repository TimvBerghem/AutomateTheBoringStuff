import random
numberOfStreaks = 0
currentHStreak = 0
currentTStreak = 0
totalExperiments = 0
for experimentNumber in range(10001):
  totalExperiments = experimentNumber
  # Code that creates a list of 100 'heads' or 'tails' values.
  flip = random.choice(['H', 'T'])
  if flip == 'H':
    currentHStreak += 1
    currentTStreak = 0
    if currentHStreak >= 6:
      numberOfStreaks += 1
  else:
    currentTStreak += 1
    currentHStreak = 0
    if currentTStreak >= 6:
      numberOfStreaks += 1

  # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(f'The total number of streaks is {numberOfStreaks} over {totalExperiments} tries')