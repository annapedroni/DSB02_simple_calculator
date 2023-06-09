'''
This is a simple calculator: the user can enter two numbers and the operator,
and they will get the result on the screen and in a file called 'equation_and_solution.txt'.

Alternatively, they can enter a text file containing the desired input, the solution will be printed on the screen.
They might not get a solution, but the program will not crash :P
'''
'''
NB: A lot of repetition, because I tried to solve this without lists, that had not been used yet in the course.
Also, functions could simplify all. Not there yet :)
'''


import os # needed to find the test files
          # from: https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory


# get the user input
intro_message = """\nHello!
I can perform these binary operations: sum, subtraction, multiplication, division, and exponentiation.
Please, follow the instructions to enter the first argument, the operator, and the second argument.
Press "q" to quit at any moment.
Alternatively, I can accept a file in the .txt format. It must contain one operation per line, in this format: number operator number. E.g.:
12 + 37
76 / 180
Valid operators are +, -, x or *, /, ^ or **\n"""
print(intro_message)

# choose the type of input
enter_manually = False
use_file = input("If you would like to enter the operation through a .txt file rather than manually, type 'f', any other input to continue manually: ")
if use_file.lower() == "f":
    use_file = True
    print("You chose to use a file.\n")
else:
    use_file = False
    enter_manually = True
    print("You chose to enter the data manually.\n")


# get the input

# input entered through a file
while use_file:
    file_to_open = input("Enter the name of your file with the extension(e.g. input.txt): ")
    file_to_open = file_to_open.strip()
    if file_to_open == "q":
        use_file = False
        break
    elif file_to_open[-4:] != ".txt":
        print("Not a file with a .txt extension")
    else:
        try:
            here = os.path.dirname(os.path.abspath(__file__))  # from: https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
            filename = os.path.join(here, file_to_open)        # because the location from where the script is running can be different from the one he is saved.. I'm still trying to understand
            
            with open(filename, 'r') as file:
                operation_lines = file.readlines()
                if operation_lines == []:
                    print(f"The file {file_to_open} is empty.")
                    continue
                else:
                    break
        except FileNotFoundError:        
            print(f"The file {file_to_open} does not exist.")
            # if no file, ask if go on manually or quit
            choose_again = input("\nWhat would you like to do?\nEnter data manually: m\nQuit: q\nTry another file.txt: any input :)\n> ")
            print()
            if choose_again.lower() == "q":
                use_file = False
                break
            elif choose_again.lower() == "m":
                use_file = False
                enter_manually = True
                break
            else:
                continue


# input entered through a file
while use_file:
    # for loop through lines that check the input and do the calculation (and report a line with an invalid operation)
    for line in operation_lines:
        # check if there are three terms in the line
        operation_terms = line.strip()
        first_whitespace = operation_terms.find(" ")
        if first_whitespace == -1:
            print(f"{line} is not a valid input")
            
        else:
            first_operand = operation_terms[:first_whitespace]
            operator_second_operand = operation_terms[first_whitespace:].strip()
            second_whitespace = operator_second_operand.find(" ")
            # and not more than three items
            if second_whitespace == -1 or operator_second_operand[second_whitespace+1:].strip().find(" ") != -1:
                print(f"{line} is not a valid input\n")
                
            else:
                operator = operator_second_operand[:second_whitespace]
                second_operand = operator_second_operand[second_whitespace:].strip()
                # if I have exactly three terms, try to perform the operation
                try:
                    first_operand = float(first_operand)
                    operator = operator # useless, but just to have a little order
                    second_operand = float(second_operand)
                
                    if operator == "+":
                        result = first_operand + second_operand
                    elif operator == "-":
                        result = first_operand - second_operand
                    elif operator == "x" or operator == "*":
                        result = first_operand * second_operand
                    elif operator == "/":
                        try:
                            result = round(first_operand / second_operand, 4)
                        except ZeroDivisionError:
                            result = "ERROR: the divisor cannot be 0"
                    elif operator == "^" or operator == "**":
                        operator = "to the power of"
                        try:
                            result = first_operand ** second_operand
                        except OverflowError:
                            result = "SORRY, the result is too large"
                        # output the result
                    result_message = f"{first_operand} {operator} {second_operand} = {result}\n"
                    print(result_message)        
                except:
                    print("{} is not a valid input\n".format(line))

    break




# check the input entered manually
while enter_manually:
    first_operand = input("Please, enter the first operand: ")
    if first_operand.strip() == "q":
        enter_manually = False
        break
    else:
        try:
            first_operand = float(first_operand)
            break
        except ValueError:
            print("Not a valid number. Try again.")

while enter_manually:
    operator = input("Which operation? '+'(for addition), '-' (for subtraction), '/' (for division), 'x' (for multiplication), '^' (for exponentiation): ")
    operator = operator.strip()
    if operator == "q":
        enter_manually = False
        break
    elif ( operator == "+"
        or operator == "-"
        or operator == "x"
        or operator == '/'
        or operator == "^"):
        break
    else:
        print("Not a valid operator. Try again.")

while enter_manually:
    second_operand = input("Please, enter the second operand: ")
    if second_operand.strip() == "q":
        enter_manually = False
        break
    else:
        try:
            second_operand = float(second_operand)
            break
        except ValueError:
            print("Not a valid number. Try again.")



# execute the requested operation on the input entered manually

#quit
if enter_manually == False and use_file == False: # no 'Goodbye!' if enter_manually is false because the user wants to use a file for input (use_file == True)
    print("Goodbye!")

# data entered manually
elif enter_manually == True:
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
    elif operator == "^":
        operator = "to the power of"
        try:
            result = first_operand ** second_operand
        except OverflowError:
            result = "SORRY, the result is too large"
    # output the result and save it to a file (create it if it does not exists, append to it otherwise)
    print()
    result_message = f"{first_operand} {operator} {second_operand} = {result}"
    print(result_message)
    print("(find it also in the 'equation_and_solution.txt' file)\n")
    with open("equation_and_solution.txt", "a") as solution:             # https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
        solution.write(f"{result_message}\n\n")