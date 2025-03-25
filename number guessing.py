import random
import time

def number_guessing():
    number = random.randint(1, 100)
    print(
    "I'm think of a number between 1 and 100",
    "You have 5 chances to guess the correct number.",
    "",
    "Please select the difficulty level:",
    "1. Easy (10 chances)",
    "2. Medium (5 chances)",
    "3. Hard (3 chances)",
    "",
    sep="\n"
    )
    
    while True:
        try:
            difficulty = int(input("Enter your choice: ")) - 1 # -1 to work with indexes better cuz they start at 0
            if difficulty in range(3):
                break
            else:
                print("You didn't input 1, 2, or 3, try again.")
        except ValueError:
            print("You didn't input 1, 2, or 3, try again.")
    
    chances = 10 // (difficulty + 1) #this coincidentally works
    difficulty_name = "Easy" if difficulty == 0 else "Medium" if difficulty == 1 else "Hard"
    start_guessing_time = time.time()
    attempts = 1
    hints = 0
    #tuple of all possible hints
    hints_tuple = ("It is in pi. Think about that.", f"It has {len(str(number))} digits.", f"It is {"even" if number % 2 == 0 else "odd"}.", f"It starts with {str(number)[0]}.", f"It is one of these numbers: {sorted(random.choices(range(1, 101), k=9) + [number])}.")
    
    print(f"\nGreat! You have selected the {difficulty_name} difficulty level.")
    print("Let's start the game!")
    
    while attempts <= chances:
        guess = input("\nEnter your guess: ")

        #hints
        try:
            guess = int(guess)
        except:
            if str(guess) == "hint" and attempts > 1:
                print(hints_tuple[random.randint(0,attempts // 2) + difficulty])
                hints += 1
                continue
            elif str(guess) == "hint":
                print("You haven't guessed yet! How are you even stuck.")
                continue
            else:
                print("You didn't input a number or hint.")
                continue
        
        #number guesses
        if int(guess) > number:
            print(f"Incorrect! The number is less than {guess}.")
        elif int(guess) < number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempt{"s" if attempts > 1 else ""}.")
            end_guessing_time = time.time()
            guessing_time = end_guessing_time - start_guessing_time
            score = [difficulty_name, attempts, hints, guessing_time]
            high_score[difficulty] = score if high_score[difficulty][1:-1] > score[1:-1] else high_score[difficulty]
            print(f"Your score is {score[1]} attempt{"s" if score[1] > 1 else ""} in {score[3]:.3f} seconds with {hints} hint{"" if hints == 1 else "s"} for {score[0]} difficulty.")
            break
        attempts += 1

    #losing screen
    else:
        print(f"The number was {number}.")

    print(f"Your high score is {high_score[difficulty][1]} attempt{"s" if high_score[difficulty][1] > 1 else ""} with {high_score[difficulty][2]} hint{"" if hints == 1 else "s"} in {high_score[difficulty][-1]:.3f} seconds for {high_score[difficulty][0]} difficulty.")
    #the lengths I go through, to have the gramatically accurate s' ^
    #play again?
    while True:
        replay = input("\nPlay again? (Y/N):").lower()
        if replay == "y":
            print("Replaying...")
            number_guessing()
            return #if function is broken out of, means they quit it so this just breaks out of the function out of the function... till completely out
        elif replay == "n":
            print("Quitting...")
            return
        else:
            print("Input not Y or N, try again.")

#initialize scores to make lists with valid indexes
high_score = [[99] * 4 for _ in range(3)]
score = [99] * 4
print(high_score)
print("Welcome to the Number Guessing Game!") #who would say welcome multiple times
number_guessing()

print("You have quit. :(")
