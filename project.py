import random

while True:
    hand = str(input()).lower()

    if hand == "quit":
        break

    if hand != 'rock' and hand != 'paper' and hand != 'scissor':
        print("enter correct input")
        continue

    computer_hand = random.choice(['rock','paper','scissor'])
    print(f"computer choosed {computer_hand} ")

    if computer_hand == hand:
        print("Tie")
        continue
    elif hand == 'paper' and computer_hand =='rock':
        print("you won")
        break
    elif hand == 'rock' and computer_hand =='scissor':
        print("you won")
        break
    elif hand == 'scissor' and computer_hand =='paper':
        print("you won")
        break
    else:
        print("you lost")
