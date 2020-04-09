########### Comma code ############

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(lijst):
    count = 0
    joined = ''
    try:
        while count < len(lijst) - 2:
            joined = joined + lijst[count] + ', '
            count += 1
        joined = joined + lijst[-2] + ' and '
        joined = joined + lijst[-1] + '.'
    except(IndexError):
        print('The list is empty!')
    print(joined)

comma(spam)