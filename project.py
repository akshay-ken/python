import random

def game():
    hand = str(input())
    random_hand = random.choice(['rock','paper','secior'])
    while hand.lower() == random_hand:
        print(f"you win you enterd {hand} and computer choosed {random_hand} ")
        break    
    else:
        print("try again")
        hand = str(input())


game()
        
