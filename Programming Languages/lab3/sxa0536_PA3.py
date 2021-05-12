"""
Shubham Arya
1001650536
April 25, 2021
MacOS Big Sur
"""

# opening and reading file
file = open("input.txt","r")
lines = file.readlines()

"""
global variables used throughout the code
stack- contains braces. { is appended to the stack, while } pops the stack.
ignoredCharacters- characters i want my program to ignore
multilineComment- check for multiline comment with /* ... */
output- this has the output string for each line
"""
stack = list()
ignoredCharacters = [";","=",".","!",":"]
multiLineComment = False
ouptut = ''

# This function processes a line from textfile and checks if it has matching braces.
def process(line):
    # lineStack- each line has its own stack as well
    # popStack- tells how many times to pop the stack
    # previous- store the previous character on the same line
    lineStack = list()
    popStack = 0
    previous = ''
    global multiLineComment
    
    # loops through each character in the line
    for char in line:
        if multiLineComment == False:
            # if the charcater is alpha numberic or part of the ignored characters, continue.
            if char.isalnum() or char in ignoredCharacters:
                continue
            # checks for quotations so it can avoid curly braces inside quotes.
            elif char == '"':
                if '"' in lineStack:
                    lineStack.pop()
                else:
                    lineStack.append(char)
            # checks if the line has comment so it can avoid curly braces inside quotes
            elif previous == '/' :
                if char == '*':
                    multiLineComment = True
                break
            # inserts ( in lineStack
            elif char == '(':
                lineStack.append(char)
            # checks if ( and ) match in the lineStack
            elif char == ')':
                if len(lineStack) > 0:
                    lineStack.pop()
                else:
                    print("Invalid syntax")
                    exit()
            # check for { as long as it is not in quotes
            elif char == "{" and '"' not in lineStack :
                stack.append(char)
            # increases pop counter as long as it not part of quotes
            elif char == "}" and '"' not in lineStack :
                popStack += 1
        else:
            if previous == '*' and char == '/':
                multiLineComment = False
        previous = char
    
    # if the lineStack is not empty, then there is a mismatch of "" or (). If it is empty, then print out the output
    if len(lineStack) > 0:
        print("Invalid syntax")
        exit()
    else:
        output = str(len(stack)) + " " + filteredLine
        print(output)
        if popStack > 0:
            # pops the stack 
            while popStack > 0:
                if len(stack) == 0:
                    print("Invalid syntax. Unmatched braces.")
                    exit()
                else:
                    stack.pop()
                popStack -= 1
        

# runs through the textfile and feeds the proces function with line.
for line in lines:
    filteredLine = line.replace("\n","")
    process(filteredLine)
  
# does a final check to see if the braces match or not
if len(stack) != 0:
    print("Invalid syntax. Unmatched braces.")
else:
    print("0 //end of program")
