import random 
print("Welcome to the Number Guessing Game!")
print("================================")
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("================================")
players = int(input("Enter the number of players: "))
while players not in (1, 2):
    print("Invalid input. Please enter 1 or 2.")
    players = int(input("Enter the number of players: "))
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
difficulty = int(input("Enter the difficulty level (1-3): "))
while difficulty < 1 or difficulty > 3:
    print("Invalid input. Please enter a number between 1 and 3.")
    difficulty = int(input("Enter the difficulty level (1-3): "))
if difficulty == 1:
    max_number = 10
    chances = 5
elif difficulty == 2:
    chances = 7
    max_number = 50
else:
    chances = 10
    max_number = 100
print("You chose difficulty level", difficulty)
print("I'm thinking of a number between 1 and", max_number)
print("You have", chances, "chances to guess the number.")
if players == 1:
    print("------ SINGLE PLAYER MODE ------")
    secret_number = random.randint(1, max_number)
    for i in range(1, chances+1):
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > max_number:
            print("Invalid input. Please enter a number between 1 and", max_number)
            continue 
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the number in", i, "chances.")
            break  
    else:
        print("Sorry, you ran out of chances. The number was", secret_number)
elif players == 2:  
    print("------ TWO PLAYER MODE ------")
    secret_number = random.randint(1, max_number)
    for i in range(1, chances+1):
        if i % 2 == 1:
            print("Player 1's turn.")
        else:
            print("Player 2's turn.")
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > max_number:
            print("Invalid input. Please enter a number between 1 and", max_number)
            continue
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            if i % 2 == 1:
                print("Congratulations Player 1! You guessed the number in", (i + 1) // 2, "turns.")
            else:
                print("Congratulations Player 2! You guessed the number in", i // 2, "turns.")
            break



