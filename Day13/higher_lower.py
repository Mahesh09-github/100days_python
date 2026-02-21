import random
from day13_data import data
def compare_profiles(a,b):
    """
    Docstring for compare_profiles
    
    :param a: Description
    :param b: Description
    It is a function which compare the follwer_count of the profiles for given a,b and return higher one
    """
    if data[a]["follower_count"] > data[b]["follower_count"]:
        return "A"
    elif data[a]["follower_count"] < data[b]["follower_count"]:
        return "B"
    else:
        None

def higher_lower_game():
    score = 0
    should_confirm = True
    B = random.randint(0,8)
    while should_confirm:
        A = B
        print(f"Compare A: {data[A]["name"]}, {data[A]["description"]}")
        print('''
                     ____   ____     
                     \   \ /   /_____
                      \   Y   /  ___/
                       \     /\___ \ 
                        \___//____  >
                                  \/ 
                ''')
        B = random.randint(0,8)
        if B == A:
            B = random.randint(0,9)
        print(f"Compare B: {data[B]["name"]}, {data[B]["description"]}")
        result = compare_profiles(A,B)
        value = input("Who has more followers? Type 'A' or 'B': ")
        if value != result:
            print(f"Sorry,that's wrong . Final score: {score}")
            should_confirm = False
        else:
            score+=1
            print(f"You are right! Current Score: {score}")

higher_lower_game()