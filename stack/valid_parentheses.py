'''
RAMPER

R - restate the problem
    given different style of brackets 
    return a boolean if and only if open brackets close of the same type 
    they must be closed in the correct order 
A - ask a question 
    don't have a question right now 
M - make an exmaple 
    ')()'
    False
    '(())'
    True 
P - pick a pattern
    hashmap / stack
E - explain the plan
    create parings of close bracket keys wither their open bracket values
    if we see a open bracket in the hashmap values
        append that to thestack
    else
        if stack isn't empty and the bottom of the stack == myMap[closingBracket]
            pop the stack
    if the stack is empty return True else return False 
'''
def isValid(s):
    myMap = {')':'(', '}':'{', ']':'['}
    stack = []
    for bracket in s:
        if bracket in myMap.values():
            stack.append(bracket)
        elif stack and stack[-1] == myMap[bracket]:
            stack.pop()
        elif break == myMap:
            return False
    return len(stack) == 0

