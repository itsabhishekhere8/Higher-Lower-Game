import random
from game_data import data
from art import logo, vs
import os
def format_data(account):
    '''take account as input aned return format printable data'''
    account_name = account['name']
    account_descrp = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descrp}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
    '''Take the user input and follower count and check for the answer'''
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

# Display Logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make game repeatable
while game_should_continue:
    # Generate random
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare {format_data(account_a)}")
    print(vs)
    print(f"Against {format_data(account_b)}")

    # Asking the user 
    guess = input("Who has more follower? Type 'a' or 'b': ").lower()

    os.system('cls')
    # Get Follower count for both the accounts
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count,b_follower_count)

    # Giving user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current Score : {score}")
    else:
        print(f"Sorry, that's wrong. Final Score : {score}")
        game_should_continue = False