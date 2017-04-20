#Hangman Script
#importing the time module
import time

#welcoming the user
name = input("What is your name?")
print("Hello,", name,". Time to play hangman!")

#wait for 2 second
time.sleep(2)
print("Start guessing...")
time.sleep(0.5)

#here we set the secret
word = "secret"
#creates an variablel with an empty value
guesses = ''
#the number of turns
turns = 10
#check if the turns are more than zero
while turns > 0:
    # a fail counter that starts with 0
    failed = 0

    for char in word:
        #if the character is in the players guesses
        if char in guesses:
            #print the character
            print(char)
        else:
            #if not found, print a dash
            print("_")
            failed += 1

    #if failed is equal to zero
    #print you won
    if failed == 0:
        print("You won!")
        #exit
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong.")
        print("You have ", turns, "more chances to guess")
        if turns == 0:
            print("You lose!")
