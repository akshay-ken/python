msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [0, 1, 2, 3, 4, 5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def check(v1, v2, v3):
    msg = ''
    v1 = float(v1)
    v2 = float(v2)
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
        msg
    if (v1 == 1 or v2 == 1) and (v3 == '*'):
        msg = msg + msg_7
        msg
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
        msg
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    v = float(v)
    output = None
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


memory = 0.0
counter = 0
while counter == 0:
    print("Enter an equation")
    x, oper, y = input().split()
    try:
        if x == 'M':
            x = float(memory)
        else:
            float(x)
        if y == 'M':
            y = float(memory)
        else:
            float(y)
        if oper in '+-*/':
            check(x, y, oper)
            if oper == '/' and float(y) == 0:
                print("Yeah... division by zero. Smart move...")
            else:
                if oper == '+':
                    result = float(x) + float(y)
                    print(result)
                elif oper == '-':
                    result = float(x) - float(y)
                    print(result)
                elif oper == '*':
                    result = float(x) * float(y)
                    print(result)
                elif oper == '/' and float(y) != 0.0:
                    result = float(x) / float(y)
                    print(result)
                print("Do you want to store the result? (y / n):")
                answer = input()
                if answer == 'y':
                    if is_one_digit(result):
                        msg_index = 10
                        print(msg_[msg_index])
                        answer = input()
                        if answer == 'y':
                            while msg_index < 12:
                                msg_index = msg_index + 1
                                print(msg_[msg_index])
                                answer = input()
                                if answer == 'y':
                                    continue
                                else:
                                    break
                            else:
                                memory = result
                    else:
                        memory = result
                print("Do you want to continue calculations? (y / n):")
                answer = input()
                if answer == 'n':
                    counter += 1
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except (TypeError, ValueError):
        print("Do you even know what numbers are? Stay focused!")
