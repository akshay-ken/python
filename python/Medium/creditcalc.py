import math
import argparse


# taking choice
parser = argparse.ArgumentParser(description='taking loan values')
parser.add_argument('-t', '--type', choices=['diff', 'annuity'], help='Incorrect parameters')
parser.add_argument('-p1', '--principal', help='add principal amount of loan')
parser.add_argument('-p2', '--periods', help='months')  # number of months needed to repay the loan
parser.add_argument('-p3', '--payment', help='Incorrect parameters')  # monthly payment amount
parser.add_argument('-i', '--interest', help='interest percent on principal amount annually')

# parsing arguments
args = parser.parse_args()

if args.type:
    # interest needed for both method
    if args.interest:
        # i = nominal interest rate
        i = float(args.interest) / (12 * 100)
        # for annuity
        if args.type == 'annuity':
            # n = number of payments
            #n = int(args.periods)
            # non-negative numbers
            #if n > 0:
            if args.principal:
                pass
            else:
                n = int(args.periods)
                A = int(args.payment)
                p = A / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
                print(f'Your loan principal = {p}!')
                overpayment = ((A) * n) - p
                print(f'Overpayment = {overpayment}')
            # for periods or n
            if args.payment:
                pass
            else:
                n = int(args.periods)
                p = int(args.principal)
                A = p * ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))

                overpayment = (math.ceil(A) * n) - p
                print(f'Your annuity payment = {math.ceil(overpayment)}!')
                print(f'Overpayment = {math.ceil(A)}')

            if args.periods:
                pass
            else:
                A = int(args.payment)
                p = int(args.principal)
                months = math.log(float(args.payment) / (float(args.payment) - i * float(p)), i + 1)
                months = math.ceil(months)

                month = months % 12
                year = months // 12
                if month == 0:
                    print(f'It will take {year} years to repay this loan!')
                    overpayment = ((A) * months) - p
                    print(f'Overpayment = {overpayment}')
                elif year == 0:
                    print(f'It will take {month} months to repay this loan!')
                    overpayment = ((A) * n) - p
                    print(f'Overpayment = {overpayment}')
                else:
                    print(f'It will take {year} years and {month} months to repay this loan!')
                    overpayment = ((A) * n) - p
                    print(f'Overpayment = {overpayment}')


            # else:
            #     print('Incorrect parameters')






        if args.type == 'diff':
            if args.payment:
                print('Incorrect parameters')
            if int(args.periods) < 0:
                print('Incorrect parameters')
            if args.interest:
                p = int(args.principal)
                n = int(args.periods)
                m = 1
                A = 0
                while m <= n:
                    D = (p / n) + (i * (p - (p * (m - 1))/n))
                    A += math.ceil(D)
                    print(f'Month {m}: payment is {int(D)}')
                    m += 1
                overpayment = (int(A)) - p
                print(f'Overpayment = {overpayment}')
            else:
                print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
# if choice == 'a':
#     print('Enter the loan principal:')
#     p = int(input())
#     print('Enter the number of periods:')
#     n = int(input())
#     n = n
#     print('Enter the loan interest:')
#     i = float(input())
#     i = i / (12 * 100)
#     a = p * ((i * ((1 + i)**n)) / (((1 + i)**n) - 1))
#     a = math.ceil(a)
#     print(f'Your monthly payment = {a}!')
#
# if choice == 'p':
#     print('Enter the annuity payment:')
#     A = float(input())
#     print('Enter the number of periods:')
#     n = int(input())
#     print('Enter the loan interest:')
#     i = float(input())
#     i = i / (12 * 100)
#     P = A / ((i * ((1 + i)**n)) / (((1 + i)**n) - 1))
#     print(f'Your loan principal = {P}!')
