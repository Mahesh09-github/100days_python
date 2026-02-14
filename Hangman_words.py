#importing library
import random
from hangman_wordslist import word_list
from hangman_art import HANGMAN_ART,logo

print("Welcome to the Hangman Game!!")
print(logo)

#choosing ramdom word
chosen_word = random.choice(word_list).lower()
print(chosen_word)

placeholder=""
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)
#intializing list
game_over = False
correct_letters=[]
lives=6
#Using while loop
while not game_over:

    print(f"****************************{lives}/7 LIVES LEFT************************")
    guess = input()

    if guess in correct_letters:
        print(f"You have already Guessed this letter: {guess}")
    
    display=""

    for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
            
    print("word to guess: " + display)
 
    if guess not in chosen_word:
        lives-=1
        print("Sorry, You have schoosen the wrong letter.")

        if lives == 0:
            game_over = True
            print("Sorry, You lose")
            print("************************YOU LOSE**************************")
    if "_"  not in display:
        game_over = True
        print("************************YOU WIN*****************************")
    print(HANGMAN_ART[lives])
    if display ==chosen_word:
        game_over = True
        print("Congrats , You Win!!")
