def loss_function():
    print("Incorrect. Unfortunately you are out of the game. Better Luck Next Time.")
    print("You earned: $" + str(moneyEarned))
    quit()

def win_function():
    print("Correct! You have won $" + str(moneyEarned) + "!\n")

# Introductory Message
print("\n\nWelcome to \"Who wants to be a Millionaire\"")
print("Coded by Aragya Goyal\n")

# Ask user if they would like to play
playing = input("Do you want to play? \n").lower()
if (playing != "yes" and playing != "y"):
    quit()
print("Let's Play!")

# Extra Variables
moneyEarned = 0

# Question 1
answer = input("Who wrote the novel \"1984\"?\n").lower()
if (answer == "george orwell"):
    moneyEarned = 100
    win_function()
else:
    loss_function()

# Question 2
answer = input("What language is spoken in Brazil?\n").lower()
if (answer == "portuguese"):
    moneyEarned = 200
    win_function()
else:
    loss_function()

# Question 3
answer = input("What does NASA stand for?\n").lower()
if (answer == "national aeronautics and space administration"):
    moneyEarned = 300
    win_function()
else:
    loss_function()

# Question 4
answer = input("What is the capital city of Canada?\n").lower()
if (answer == "ottawa"):
    moneyEarned = 500
    win_function()
else:
    loss_function()

# Question 5
answer = input("Who discovered penicillin?\n").lower()
if (answer == "alexander fleming"):
    moneyEarned = 1000
    win_function()
    print("10 more questions left!")
else:
    loss_function()

# Question 6
answer = input("In what year was Facebook founded?\n").lower()
if (answer == "2004"):
    moneyEarned = 2000
    win_function()
else:
    loss_function()

# Question 7
answer = input("In what country are the 2024 Summer Olympics held?\n").lower()
if (answer == "france"):
    moneyEarned = 4000
    win_function()
else:
    loss_function()

# Question 8
answer = input("What is the longest river in the world?\n").lower()
if (answer == "nile river"):
    moneyEarned = 8000
    win_function()
else:
    loss_function()

# Question 9
answer = input("What word describes a word that spells the same backward and forwards?\n").lower()
if (answer == "palindrome"):
    moneyEarned = 16000
    win_function()
else:
    loss_function()

# Question 10
answer = input("How many claws does a domestic cat usually have?\n").lower()
if (answer == "18"):
    moneyEarned = 32000
    win_function()
    print("5 more questions left!")
else:
    loss_function()

# Question 11
answer = input("Which fruit is the most popular and consumed worldwide?\n").lower()
if (answer == "tomato"):
    moneyEarned = 64000
    win_function()
else:
    loss_function()

# Question 12
answer = input("How many stars are there on the flag of China?\n").lower()
if (answer == "5"):
    moneyEarned = 125000
    win_function()
else:
    loss_function()

# Question 13
answer = input("How many constellations are recognized by the International Astronomical Union?\n").lower()
if (answer == "88"):
    moneyEarned = 250000
    win_function()
else:
    loss_function()

# Question 14
answer = input("Which country produces the most chocolate?\n").lower()
if (answer == "ivory coast"):
    moneyEarned = 500000
    win_function()
else:
    loss_function()

# Question 15
answer = input("What is the smallest bone in the human body called?\n").lower()
if (answer == "stapes"):
    moneyEarned = 1000000
    win_function()
    print("Congratulations! You are a Millionaire!")
else:
    loss_function()