import random

# is_sum function returns sum of list
def is_sum(list):
    sum=0
    for i in list:
        sum += i
    return sum

def deal_cards(c):
    return random.choices(c, k = 2)

#deck of cards (11 is the ace)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#main function
def main():
    user_cards = deal_cards(cards)
    computer_cards = deal_cards(cards)
    should_confirm = False
    while not should_confirm:
        user_score = is_sum(user_cards)
        computer_score = is_sum(computer_cards)
        print(f"Player cards :{user_cards}, Player score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        if user_score == 21:
            print("User Wins!!")
            break
        elif computer_score == 21:
            print("Computer Wins!!")
            break
        elif user_score > 21:
            if 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_score = is_sum(user_cards)
                if user_score > 21:
                    print("Lose")
                    break
            else:
                print("Computer Wins!!")
                should_confirm = True
        else:
            draw = input("Do you want to draw another card ?type 'y' or 'n'")
            if draw == 'y':
                user_cards.append(random.choice(cards))
            else:
                should_confirm = True
                if computer_score < 16:
                    computer_cards.append(random.choice(cards))
                    computer_score = is_sum(computer_cards)
                    if computer_score == 21:
                        print("Computer Wins!!")
                    elif computer_score > 21:
                        print("User Win!!")
                    else:
                        if user_score > computer_score:
                            print("User Win!!")
                        elif computer_score > user_score:
                            print("Computer Wins!!")
                        else:
                            print("Draw")


main()