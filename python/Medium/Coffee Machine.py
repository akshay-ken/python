machine_water = 400
machine_milk = 540
machine_coffee_beans = 120
machine_cups = 9
machine_money = 550


def ingredients_calculator(water=0, milk=0, coffee_beans=0, cost=0, cups=0, ask=False, re=False, buy=False, fill=False):
    global machine_water, machine_money, machine_cups, machine_milk, machine_coffee_beans

    if buy:
        if machine_water < water:
            print('Sorry, not enough water!')
        elif machine_milk < milk:
            print('Sorry, not enough milk!')
        elif machine_cups < cups:
            print('Sorry, not enough cups!')
        elif machine_coffee_beans < coffee_beans:
            print('Sorry, not enough coffee beans!')
        else:
            print('I have enough resources, making you a coffee!')
            machine_water -= water
            machine_milk -= milk
            machine_coffee_beans -= coffee_beans
            machine_cups -= cups
            machine_money += cost
    if fill:
        machine_water -= water
        machine_milk -= milk
        machine_coffee_beans -= coffee_beans
        machine_cups -= cups
    if ask:
        machine_money += cost
    if re:
        print(f'''\nThe coffee machine has:
{machine_water} ml of water
{machine_milk} ml of milk
{machine_coffee_beans} g of coffee beans
{machine_cups} disposable cups
${machine_money} of money''')


def fill_logic():
    current_amount_of_ingredients_to_add = {
        'add_water': '\nWrite how many ml of water you want to add: ',
        'add_milk': 'Write how many ml of milk you want to add: ',
        'add_coffee_beans': 'Write how many grams of coffee beans you want to add: ',
        'add_cups': 'Write how many disposable cups of coffee you want to add: '}

    for item in current_amount_of_ingredients_to_add:
        print(current_amount_of_ingredients_to_add[item])
        current_amount_of_ingredients_to_add[item] = int(input())
    water = current_amount_of_ingredients_to_add['add_water']
    milk = current_amount_of_ingredients_to_add['add_milk']
    coffee_beans = current_amount_of_ingredients_to_add['add_coffee_beans']
    cups = current_amount_of_ingredients_to_add['add_cups']

    ingredients_calculator(water=- int(water), milk=- int(milk), coffee_beans=- int(coffee_beans), cups=- int(cups), fill=True)


def buy_action():
    print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    option = input()

    if option == '1':
        ingredients_calculator(water=250, milk=0, coffee_beans=16, cost=4, cups=1, buy=True)
    elif option == '2':
        ingredients_calculator(water=350, milk=75, coffee_beans=20, cost=7, cups=1, buy=True)
    elif option == '3':
        ingredients_calculator(water=200, milk=100, coffee_beans=12, cost=6, cups=1, buy=True)
    elif option == 'back':
        pass


def take_logic():
    global machine_money
    money = machine_money
    print(f'I gave you ${money}\n')
    ingredients_calculator(cost=-money, ask=True)


while True:
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        buy_action()
    elif action == 'fill':
        fill_logic()
    elif action == 'take':
        take_logic()
    elif action == 'remaining':
        ingredients_calculator(re=True)
    elif action == 'exit':
        break
