import random
import sys
import time

print("==============================")
print("WELCOME TO GUESS THE NUMBER!!!")
print("==============================")


def tryagain():
    print("Would you like to play again?")
    again = input(("type e for Easy, h for Hard, and any other key to exit: "))
    if (again == 'e' or again == 'E'):
        Easy()
    elif (again == 'h' or again == 'H'):
        Hard()
    else:
        sys.exit()


def Easy():
    print("=======================")
    print("WELCOME TO EASY MODE!!!")
    print("=======================")
    time.sleep(2)
    user_guess = int(input("Guess a number between 1-10: "))
    comp_no = random.randint(1, 10)

    while(user_guess != comp_no):
        if (user_guess > comp_no):
            print("Your guess was too high!")
            print("Try again")
            time.sleep(1)
            user_guess = int(input("Guess a number between 1-10: "))
        elif (user_guess < comp_no):
            print("Your Guess was too low!")
            print("Try again")
            time.sleep(1)
            user_guess = int(input("Guess a number between 1-10: "))
    print("==================================")
    print("WELL DONE YOU GUESSED CORRECTLY!!!")
    print("==================================")


def Hard():
    print("=======================")
    print("WELCOME TO HARD MODE!!!")
    print("=======================")
    time.sleep(2)
    print("In this mode you only have 3 tries to guess correctly goodluck :)")
    count = 0
    comp_no2 = 4  # random.randint(1, 11)
    while (count <= 3):
        user_guess2 = int(input("Guess a number between 1-10: "))
        count = count + 1
        if (user_guess2 > comp_no2):
            print("Your guess was too high!")
            print("Try again")
            time.sleep(1)
        elif (user_guess2 < comp_no2):
            print("Your Guess was too low!")
            print("Try again")
            time.sleep(1)
        if(count == 3 and user_guess2 != comp_no2):
            print("============")
            print("EPIC FAIL!!!")
            print("============")
            break
        if(count <= 3 and user_guess2 == comp_no2):
            print("==============================")
            print("WELL DONE YOU GUESSED CORRECTLY!!!")
            print("==============================")
            break


time.sleep(1)
print("There are two modes")
user_select_mode = input("Please enter e for easy for h for hard: ")
if (user_select_mode == 'e' or user_select_mode == 'E'):
    Easy()
elif (user_select_mode == 'h' or user_select_mode == 'H'):
    Hard()
else:
    sys.exit()
tryagain()
