import random
import art
def guess_num():
    return random.randint(1, 100)

def difficulty_level():
    while True:
        game_level = input("Enter the difficulty level. Type 'easy' or 'hard': ").lower()
        if game_level == 'easy':
            return 10  # Easy mode gives 10 attempts
        elif game_level == 'hard':
            return 5  # Hard mode gives 5 attempts
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")

def gameplay():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = guess_num()
    attempts = difficulty_level()
    game_over = False
    while not game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if user_guess == number:
            print(f"That's it! You guessed the correct answer: {number}.")
            game_over = True
        elif user_guess < number:
            print("Too LOW! Guess again.")
        else:
            print("Too HIGH! Guess again.")
        attempts -= 1
        if attempts == 0 and not game_over:
            print(f"You've run out of attempts!! The number was {number}.Try Again.")
            game_over = True



gameplay()
again=input("Do you want to try again?Type 'Yes' to play again or 'No' to quiet game." ).lower()
if again=='yes':
    print("\n"*50)
    gameplay()
else:
    print("Bye Thank You for playing the game.Come Again...")
