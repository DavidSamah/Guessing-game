import random 
def safe_int(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            return int(text)
        print("Please enter a whole number.")

def choose_difficulty():
    print("Choose a difficulty level: ")
    print(" 1 - Easy(10 guesses)")
    print(" 2  Medium(7 guesses)")
    print(" 3 - Hard(5 guesses)")
    while True:
        choice = input("Enter 1 , 2, or 3: ").strip()
        if choice == "1":
            return 10
        if choice == "2":
            return 7
        if choice == "3":
            return 5
        print("Invalid choice, Try again.")

def play_game():
    print("\n Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    attempts_left = choose_difficulty()
    secret = random.randint(1, 100)

    while attempts_left > 0:
        print(f"\nYou have {attempts_left} guesses remaining.")
        guess  = safe_int("Guess a number: ")
        if guess == secret:
            print("Correct! You win!")
            return
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")
        attempts_left -= 1

        print(f"Out of guesses! The number was {secret}.")

def main():
    print("Simple Python game: Guess the Number.")
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing! ")
            break
if __name__ == "__main__":
    main()



    
        