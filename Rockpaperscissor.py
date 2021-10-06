from random import randint
import time

options = ['Rock','Paper','Scissors']
computerscore = 0
playerscore = 0
stopper = 'Yes'

while stopper == 'Yes' or stopper == 'yes' or stopper == 'Yeah' or stopper == 'yeah':
    computerchoice = options[randint(0,2)]
    playerchoice = input("Choose Rock,Paper or Scissors: ")
    if computerchoice == playerchoice :
        print(f'Computer has chosen {computerchoice}')
        time.sleep(2)
        print('Tie! Score was unchanged')
    
    elif (playerchoice == 'Rock') :
        if (computerchoice == options[1]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You lost! Paper covers Rock!")
            computerscore+=1
        elif (computerchoice == options[2]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You won!Rock smashes Scissors!")
            playerscore+=1
    elif (playerchoice == 'Paper') :
        if (computerchoice == options[0]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You won! Paper covers Rock!")
            playerscore+=1
        elif (computerchoice == options[2]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You lost! Scissors cut paper!")
            computerscore+=1
    elif (playerchoice == 'Scissors') :
        if (computerchoice == options[0]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You lost!Rock smashes Scissors!")
            computerscore+=1
        elif (computerchoice == options[1]) :
            print(f'Computer has chosen {computerchoice}')
            time.sleep(2)
            print("You won! Scissors cut paper!")
            playerscore+=1
    else :
        print("Please enter a valid choice")
    print(f'Current score is {computerscore} for the computer, your score is {playerscore}')
    stopper = input("Do you wish to continue?  ")
