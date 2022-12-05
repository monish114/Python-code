import random

def compare_numbers(number, user_guess):
    cow=0 
    bull=0 
    for x in range(4): 
        if user_guess[x] == number[x]:
            bull = bull + 1
        else: 
            cow = cow + 1
    cowbull =[cow, bull]  
    return cowbull

playing = True 
number = str(random.randint(1000,9999)) 
guesses = 0
print(number)

print("Let's play a game of Cowbull!") 
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break 
    else:
        print("Your guess isn't quite right, try again.")
