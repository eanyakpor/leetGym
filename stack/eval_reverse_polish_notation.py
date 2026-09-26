'''
RAMPER
R - restate the problem
    given a string of numbers and operands '+', '*', '/', '-'
    return a value following PEMDAS / reverse polish notation
A - ask any question 
    will there always be an awsner? 
M - make an example 
    ['2','3','-']
    -1 
    ['0','0','+']
    0
P - pick a pattern
    stack
E - explain the pattern
    follow LIFO
    append numbers 
    pop on non number the first two chareactrs 
    in stack then peform operation 
    save the result
    repeat this action until we've reached the end of the array

tokens = ["2","1","+","3","*"]

'''
def evalRPN(tokens):
    stack = []
    # string operand to operand hashmap
    operandSet = {'+', '-', '*', '/'}
    for char in tokens:
        if char not in operandSet:
            # its a number
            stack.append(int(char))
        else:
            rightNum = stack.pop()
            leftNum = stack.pop()

            if char == '+':
                stack.append((leftNum + rightNum))
            elif char == '-':
                stack.append((leftNum - rightNum))
            elif char == '*':
                stack.append((leftNum * rightNum))
            else:
                stack.append(int(leftNum / rightNum))
    return stack[-1]


