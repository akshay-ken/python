
# creating matrix to analyzing wining pattern
M1 = " "
M2 = " "
M3 = " "
M4 = " "
M5 = " "
M6 = " "
M7 = " "
M8 = " "
M9 = " "


# using printer to update values in real time
def printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9):
    print('---------\n| ' + m1 + ' ' + m2 + ' ' + m3 + ' |\n| ' + m4 + ' ' + m5 + ' '
          + m6 + ' |\n| ' + m7 + ' ' + m8 + ' ' + m9 + ' |\n---------')


def game_logic():
    global M1, M2, M3, M4, M5, M6, M7, M8, M9
    # storing wins
    x_wins = 0
    o_wins = 0
    count_empty = 0  # count empty cells in grid

    # finding patters
    x = 'X'  # for ease of typing x variable instead of string 'X'
    o = 'O'
    # |
    # |
    # |
    if (x == M1) and (x == M4) and (x == M7):
        x_wins += 1  # when the grid has three X's in a row (including diagonals).
    if (o == M1) and (o == M4) and (o == M7):
        o_wins += 1  # when the grid has three O's in a row (including diagonals).
    #  |
    #  |
    #  |
    if (x == M2) and (x == M5) and (x == M8):
        x_wins += 1
    if (o == M2) and (o == M5) and (o == M8):
        o_wins += 1
    #   |
    #   |
    #   |
    if (x == M3) and (x == M6) and (x == M9):
        x_wins += 1
    if (o == M3) and (o == M6) and (o == M9):
        o_wins += 1
    # ---
    #
    #
    if (x == M1) and (x == M2) and (x == M3):
        x_wins += 1
    if (o == M1) and (o == M2) and (o == M3):
        o_wins += 1
    #
    # ---
    #
    if (x == M4) and (x == M5) and (x == M6):
        x_wins += 1
    if (o == M4) and (o == M5) and (o == M6):
        o_wins += 1
    #
    #
    # ---
    if (x == M7) and (x == M8) and (x == M9):
        x_wins += 1
    if (o == M7) and (o == M8) and (o == M9):
        o_wins += 1
    # x
    #  x
    #   x
    if (x == M1) and (x == M5) and (x == M9):
        x_wins += 1
    if (o == M1) and (o == M5) and (o == M9):
        o_wins += 1
    #   x
    #  x
    # x
    if (x == M3) and (x == M5) and (x == M7):
        x_wins += 1
    if (o == M3) and (o == M5) and (o == M7):
        o_wins += 1
    for symbol in [M1, M2, M3, M4, M5, M6, M7, M8, M9]:
        if symbol == ' ':
            count_empty += 1
    # calling final winner
    choosing_winner(x_wins, o_wins, count_empty)


game_on = True


def choosing_winner(x_wins, o_wins, count_empty):
    global game_on
    # when x_wins variable holds value 1 and o_wins variable holds value 0 then X wins
    if (x_wins == 1) and (o_wins == 0):
        print('X wins')
        game_on = False
    if (o_wins == 1) and (x_wins == 0):
        print('O wins')
        game_on = False
    # when no side has a three in a row and the grid has no empty cells.
    if (x_wins == 0) and (o_wins == 0) and (count_empty == 0):
        print('Draw')
        game_on = False


count = 0
moved = 'X'


def moving_logic():
    global count, moved
    if count % 2 == 0:
        moved = 'X'
    elif count % 2 == 1:
        moved = 'O'
    return moved


def updating_grid():
    global M1, M2, M3, M4, M5, M6, M7, M8, M9, count, moved, game_on
    while game_on:
        try:
            move = input()  # taking input with numbers and space as string
            row = int(move[0])  # storing first number as row
            column = int(move[2])  # ignoring space and storing second number as column
            # checking if entered number is bigger than length of grid
            if (row > 3) or (column > 3):
                print('Coordinates should be from 1 to 3!')
                # if yes then looping through code
                continue
        # checking for value and type error
        except (ValueError, TypeError):
            print('You should enter numbers!')
            continue  # if there is error then loop through code
        else:
            not_empty = 'This cell is occupied! Choose another one!'
            # first row
            if row == 1:
                if column == 1:
                    if M1 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M1 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 2:
                    if M2 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M2 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 3:
                    if M3 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M3 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
            # second row
            if row == 2:
                if column == 1:
                    if M4 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M4 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 2:
                    if M5 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M5 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 3:
                    if M6 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M6 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
            # third row
            if row == 3:
                if column == 1:
                    if M7 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M7 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 2:
                    if M8 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M8 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
                if column == 3:
                    if M9 != ' ':
                        print(not_empty)
                        continue
                    else:
                        M9 = moved
                        count += 1
                        printer(m1=M1, m2=M2, m3=M3, m4=M4, m5=M5, m6=M6, m7=M7, m8=M8, m9=M9)
                        moving_logic()
                        game_logic()
                        continue
            break


# calling functions by order
printer()
updating_grid()


