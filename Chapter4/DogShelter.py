dogList = []

def addDog():
    global dogList
    addMore = 'Yes'
    
    while addMore == 'Yes' or addMore == 'yes':
        print('\nPlease enter the name of your dog:')
        dogList = dogList + [input()]
        
        print(f'\n{dogList[-1]} will be taken good care off! \n')
        print('Do you wish to add more dogs? Yes or No:')
        addMore = input()

def showDogList():
    print(f'\nWe have {len(dogList)} of your dogs in our shelter. \nThe following dogs have been administered:')
    for dogs in dogList:
        print(f'- {dogs}')

def dogAdministration():                                                #Main program loop
    print('Welcome to the dog shelter')
    addDog()                                                            #Lets user add dogs
    showDogList()                                                       #Displays dogs left at shelter
    
dogAdministration()                                                     #Run program