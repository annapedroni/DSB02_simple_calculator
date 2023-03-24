'''
This is a simple calculator: the user can enter two numbers and the operator, and they will get the result.
Alternatively, they can enter a text file containing the desired input. They might not get a solution, but the program will not crash :P
'''


# get the user input
intro_message = """\nHello!
I can perform these binary operations: sum, subtraction, multiplication, division, and exponentiation.
Please, follow the instructions to enter the first argument, the operator, and the second argument.
Press "q" to quit at any moment.\n"""
print(intro_message)

keep_going = True

while keep_going:
    first_operand = input("Please, enter the first operand: ")
    if first_operand.strip() == "q":
        keep_going = False
        break
    else:
        try:
            first_operand = float(first_operand)
            break
        except ValueError:
            print("Not a valid number. Try again.")

while keep_going:
    operator = input("Which operation? '+'(for addition), '-' (for subtraction), '/' (for division), 'x' (for multiplication), 'e' (for exponentiation): ")
    operator = operator.strip()
    if operator == "q":
        keep_going = False
        break
    elif ( operator == "+"
        or operator == "-"
        or operator == "x"
        or operator == '/'
        or operator == "e"):
        break
    else:
        print("Not a valid operator. Try again.")

while keep_going:
    second_operand = input("Please, enter the second operand: ")
    if second_operand.strip() == "q":
        keep_going = False
        break
    else:
        try:
            second_operand = float(second_operand)
            break
        except ValueError:
            print("Not a valid number. Try again.")

# execute the requested operation
if keep_going == False:
    print("Goodbye!")
else:
    if operator == "+":
        result = first_operand + second_operand
    elif operator == "-":
        result = first_operand - second_operand
    elif operator == "x":
        result = first_operand * second_operand
    elif operator == "/":
        try:
            result = round(first_operand / second_operand, 4)
        except ZeroDivisionError:
            result = "ERROR: the divisor cannot be 0"
    elif operator == "e":
        operator = "to the power of"
        try:
            result = first_operand ** second_operand
        except OverflowError:
            result = "SORRY, the result is too large"
    # output the result
    result_message = f"\n{first_operand} {operator} {second_operand} = {result}\n"
    print(result_message)