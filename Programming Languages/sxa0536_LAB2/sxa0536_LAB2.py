"""
Shubham Arya
1001650536
04/04/2021
macOS Big Sur

Instructions:
To run the code, change directory to the one with this file. Then to run it, enter: python sxa0536_LAB2.py
This will run the python code and print out the results of the input_RPN.txt file.
"""


def compute(x, y, op):
    switcher = {
        '*': x * y,
        '+': x + y,
        '-': x - y,
        '/': x / y
    }
    return switcher.get(op, "Invalid operation.")


fileName = 'input_RPN.txt'
file = open(fileName, "r")
operations = ['+', '-', '*', '/']

# goes through each line in lines
for line in file:
    # initialize a stack for each line. keep a counter to iterate over the stack list.
    stack = []
    counter = 0

    # removes the \n from the line
    line = line.strip('\n')

    # this splits the line into words that are separated by a space.
    characters = line.split()

    for character in characters:

        # this statement is executed if the character is a number
        if not operations.__contains__(character):
            # converting the character to int for calculations, adding to stack and incrementing counter
            number = int(character)
            stack.append(number)
            counter += 1
        # check if the character is an operation, and if it is, compute the values
        else:
            # compute returns the computed values. It updates in the second last element in stack
            stack[counter - 2] = compute(stack[counter - 2], stack[counter - 1], character)
            # pop the last value in stack as it is not needed.
            # Also reduce the counter so next character can be in the same position
            stack.pop()
            counter -= 1

    print(line + " = " + str(stack[0]))

# close the file when it's done.
file.close()
