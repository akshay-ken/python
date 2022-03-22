import random

winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


def rpc_logic():
    global running, score
    user_action = input()
    valid_actions = ['rock', 'paper', 'scissors']
    if user_action == '!exit':
        print('Bye!')
        running = False
    elif user_action == '!rating':
        print(f'Your rating: {score}')
    elif user_action in valid_actions:
        computer_action = random.choice(['rock', 'paper', 'scissors'])
        # set True if  computer win
        first_condition = (user_action == 'rock') and (computer_action == 'paper')
        second_condition = (user_action == 'scissors') and (computer_action == 'rock')
        third_condition = (user_action == 'paper') and (computer_action == 'scissors')
        if user_action == computer_action:
            print(f'There is a draw {computer_action}')
            score += 50
        elif first_condition or second_condition or third_condition:
            print(f'Sorry, but the computer chose {computer_action}')
        else:
            print(f'Well done. The computer chose {computer_action} and failed')
            score += 100
    else:
        print('Invalid input')


def arpc_logic(user_input):
    global score, running
    user_list = user_input
    converted_list = user_list.split(',')
    user_action = input()
    if user_action == '!exit':
        print('Bye!')
        running = False
    elif user_action == '!rating':
        print(f'Your rating: {score}')
    elif str(user_action) in converted_list:
        computer_action = random.choices(converted_list)
        win = winning_cases[user_action]
        if user_action == computer_action[0]:
            print(f'There is a draw {computer_action[0]}')
            score += 50
        elif computer_action[0] not in win:
            print(f'Sorry, but computer chose {computer_action[0]}')
        else:
            print(f'Well done. The computer chose {computer_action[0]} and failed')
            score += 100
    else:
        print('Invalid input')


running = True
name = input('Enter your name: ')


def check_file():
    with open('rating.txt', 'r+t') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(' ')
            if name in line:
                starting_score = line[1]
                return int(starting_score)
        return 0


score = check_file()
print(f'Hello, {name}')
read_input = input()
print('Okay, let\'s start')
if read_input == '':
    while running:
        rpc_logic()
else:
    while running:
        arpc_logic(user_input=read_input)














#while running:
    #rpc_logic()
    #arpc_logic(user_input=read_input)
