import random

count = 0
right = 0

while True:
    print("""Which level do you want? Enter a number:
        1 - simple operations with numbers 2 - 9
        2 - integral squares of 11-29""")
    lvl = int(input())
    if lvl == 1 or lvl == 2:
        break
    else:
        print('Incorrect format.')

while count != 5:
    if lvl == 1:
        v1 = random.randint(2, 9)
        v2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])

        question = str(v1) + str(' ') + operation + str(' ') + str(v2)
        print(question)

        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print('Wrong format! Try again.')

        if operation == '-':
            result = v1 - v2
            if answer == result:
                right += 1
                print('Right!')
            else:
                print('Wrong!')
            count += 1

        elif operation == '+':
            result = v1 + v2
            if answer == result:
                right += 1
                print('Right!')
            else:
                print('Wrong!')
            count += 1

        elif operation == '*':
            result = v1 * v2
            if answer == result:
                right += 1
                print('Right!')
            else:
                print('Wrong!')
            count += 1
    elif lvl == 2:
        v1 = random.randint(11, 29)
        sqr = v1 * v1
        print(v1)
        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print('Wrong format! Try again.')
        if answer == sqr:
            right += 1
            print('Right!')
        else:
            print('Wrong!')
        count += 1


print('Your mark is ' + str(right) + '/5. Would you like to save the result? Enter yes or no')

store = input()
if store in ['yes', 'y', 'YES', 'Yes']:
    print('Whats is your name?')
    name = input()
    try:
        with open('results.txt', 'a') as file:
            if lvl == 1:
                file.write(name + ': ' + str(right) + '/5 in level ' + str(lvl) + '(simple operations with numbers 2-9).')
                print('The results are saved in "results.txt".')
            elif lvl == 2:
                file.write(name + ': ' + str(right) + '/5 in level ' + str(lvl) + '(integral squares 11-29).')
                print('The results are saved in "results.txt".')
    except:
        with open('results.txt', 'w') as file:
            if lvl == 1:
                file.write(name + ': ' + str(right) + '/5 in level ' + str(lvl) + '(simple operations with numbers 2-9).')
                print('The results are saved in "results.txt".')
            elif lvl == 2:
                file.write(name + ': ' + str(right) + '/5 in level ' + str(lvl) + '(integral squares 11-29).')
                print('The results are saved in "results.txt".')
else:
    pass
