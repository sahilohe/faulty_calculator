#faulty Calculator problem by Code with Harry

def faulty_calculator():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    print("Operators: Addition = + , Subtraction = - , Multiplication = * , Division = / ")
    operator = input("Enter the operator: ")

    if operator == '+':
        if first_number == 56 and second_number == 9:
            print("The addition is 77")
        else:
            print(f'The addition is {first_number + second_number}')

    elif operator == '-':
        print(f'The difference is {first_number - second_number}')

    elif operator == '*':
        if first_number == 45 and second_number == 3:
            print('The multiplication is 555')
        else:
            print(f'The multiplication is {first_number * second_number}')

    elif operator == '/':
        if first_number == 56 and second_number == 6:
            print('The qoutient is 4')

        else:
            print(f'The qoutient is {first_number / second_number}')

    else:
        print("Try running the code again")

faulty_calculator()
