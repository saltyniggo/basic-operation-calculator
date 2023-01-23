#this is a work in progress
#i will add every operation i need to this calculator whenever i need it
#i wont add unnecessary operators which i will never use for obvious reasons

#startup
print('B.O.C.')
print('Basic Operation Calculator')
print('')

#start the loop
calculate_again = 'yes'

#the loop
while calculate_again == 'yes' or calculate_again == 'y':
    #user needs to enter which operator and both numbers
    print('Please enter an operator: +, -, *, /')
    operator = input('')
    print('Please enter number 1')
    num_1 = float(input(''))
    print('Please enter number 2')
    num_2 = float(input(''))

    #here are the different operations
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)
    else:
        print('!ERROR! INVALID INPUT. PLEASE ENTER A VALID OPERATOR')
    calculate_again = input('Continue to calculate?')
