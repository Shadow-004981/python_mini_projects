
import secrets

choice_count = 0
choice_limit = 3
won = False

while choice_count < choice_limit:
    try:
        choice = int(input("Enter your choice (1-10): "))
        if choice < 1 or choice > 10:
            print("Choose a number between 1 and 10.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    choice_count += 1
    guess = secrets.randbelow(10) + 1

    if choice == guess:
        print("Correct! You won!")
        won = True
        break
    else:
        hint = "Too low!" if choice < guess else "Too high!"
        print(f"The number was {guess}. {hint} Try again.")

if not won:
    print("OOPS! You are out of guesses. Better luck next time.")
