def math():
  calculator = input('''
Type in the math operation you'd like you to perform:
+ for addition
- for subtraction
/ for division
* for multiplication
''')

  n1 = int(input('First Number: '))
  n2 = int(input('Second Number: '))

  if calculator == '+':
    print('{} + {} = ' .format(n1, n2))
    print(n1 + n2)

  elif calculator == '-':
    print('{} - {} = ' .format(n1, n2))
    print(n1 + n2)

  elif calculator == '*':
    print('{} * {} = ' .format(n1, n2))
    print(n1 + n2)

  elif calculator == '/':
    print('{} / {} = ' .format(n1, n2))
    print(n1 + n2)

  else:
    print('you dun goofed')

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        math()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

math()

again()