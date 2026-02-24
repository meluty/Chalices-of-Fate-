#Chalices of Fate - Mairead Luty
import random
import time

def displayIntro():
    print('''You enter a dim lit room;
a table with three chalices in front of you.
What you came here for is sat on the table in a locked box; however,
a note reads "you may take the treasure after drinking
from one of the chalices.One will result in you walking away
with what you desire and the others will lead to your death."''')
    print()

def chooseChalice():
    chalice = ""
    while chalice != '1' and chalice != '2' and chalice!= '3':
        print('Will you choose the chalice on your right(1), in the middle(2) or left(3)?')
        chalice = input()

    return chalice

def checkChalice(chosenChalice):
    print('You slowly pick up the chalice...')
    time.sleep(2)
    print('You take a deep breath before tilting the glass...')
    time.sleep(2)
    print('After drinking what is left, you slowly wait and wait until...')
    print()

    goodChalice = random.randint(1, 3)
    
    if chosenChalice == str(goodChalice):
        print('The box slowly opens to present the treasure to you.')
    else:
        print('You begin to cough before you feel yourself fall as everything beocomes dark.')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chaliceNumber = chooseChalice()
    checkChalice(chaliceNumber)

    print('Do you want to restart? Yes or no?')
    playAgain = input()



        
    
        
