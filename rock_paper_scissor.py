import random


computer_choice = random.choice(['scissors','rock','paper'])

user_choice = input('Do you Want - rock, paper and scissors?\n')

if computer_choice == user_choice:
    print("TIE")
elif user_choice == 'rock' and  computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('WIN')
else:
    print('you lose :  ( computer wins :D')               