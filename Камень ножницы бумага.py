#-----------------------------------------------------
#YOUTUBE - https://www.youtube.com/watch?v=HAYhkxd1AG8
#-----------------------------------------------------

import random, os
from termcolor import colored
print('KNB GAME\nrock=r\nscissors=s\npaper=p')
for i in range(11111):
    bet=['rock', 'scissors', 'paper']
    a=random.choice(bet)

    my_bet=input()
    if my_bet=='p' or my_bet=='s' or my_bet=='r':
        if my_bet=='p':
            my_bet='paper'
        if my_bet=='s':
            my_bet='scissors'
        if my_bet=='r':
            my_bet='rock'
    else:
        os.system('cls')
        print('Invalid input')
        continue

    os.system('cls')
    print('You: ' + my_bet)
    print('Enemy: ' + a)

    if my_bet==a:
        print(colored("draw!", 'cyan'))
        continue
    if my_bet=='paper':
        if a=='scissors':
            print(colored("you lose!", 'red'))
        else:
            print(colored("you win!", 'green'))
    if my_bet=='scissors':
        if a=='rock':
            print(colored("you lose!", 'red'))
        else:
            print(colored("you win!", 'green'))
    if my_bet=='rock':
        if a=='paper':
            print(colored("you lose!", 'red'))
        else:
            print(colored("you win!", 'green'))
