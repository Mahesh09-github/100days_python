import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
guess = random.randint(1,100)

#returns the number of turns
def difficulty(a):
    if a.lower() == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
#function which checks answer
def check_answer(lives,num):
    while lives > 0:
        print(f"You have {lives}  attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))
        if user_guess == num:
            print("You got it ! the answer was {num}")
            return
        elif user_guess > num:
            print("Too High.")
            lives-=1
        elif user_guess < num:
            print("Too Low")
            lives-=1
    if lives == 0:
        print("Sorry, you lost")

#Main function
def game():
    should_confirm = "y"
    while should_confirm ==  'y':
        print("Welcome o to the Number Guessing Game!! ")
        print("I'm thinking of a number between 1 and 100.")
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
        lives = difficulty(difficulty_level)
        check_answer(lives,guess)
        should_confirm = input("Would you like to Play again ? Type 'y' or 'n'")

game()