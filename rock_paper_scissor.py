import random
user_input = int(input("Enter 0 for rock , 1 for paper and 2 for scissor: "))
computer_input = random.randint(0,2)
print(computer_input)
if user_input<0 or user_input > 2:
    print("You have entered an invalid number. You lose!")
elif user_input == 0 and computer_input == 2:
    print("Congratulations,you win!!")
elif user_input == 1 and computer_input == 0:
    print("Congratulations,you win!!")
elif user_input == 2 and computer_input == 1:
    print("Congratulations ,you win!!")
elif user_input == computer_input:
    print("It's a draw!!")
else:
    print("Sorry, you lose!!")
