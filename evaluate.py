# Very badly commented program

# Implemented functions to solve infix expressions, given a string
# i'm too lazy to provide the algorithm
# 

operators = ['+', '-', '*', '/', '^']


def precedence(op : str) -> int:
    """ Returns the precedence of operator, if it exists, otherwise returns 0 """
    if op in operators[:2]:
        return 1
    elif op in operators[2:4]:
        return 2
    elif op == operators[-1]:
        return 3
    else:
        return 0
    
def evlexp(a : int, b : int, op : str) -> int:
    """ Evaluates basic arithmetic operation and returns it. """
    o = {'+' : a + b, '-' : a - b, '*' : a * b, '/' : a / b, '^' : a**b}
    return o[op]

def evlt(inp : str) -> int:
    """ Evaluates the passed string and returns the value if
        successful, otherwise raises an error """
    operand = [] # stack for operands
    operator = [] # stack for operators + parentheses
    i = 0 # loop variable, cannot do range because have to increment dynamically
    while i < len(inp): # while not EOF
        if inp[i].isdigit(): # if character is a digit
            num = ""
            while i < len(inp) and inp[i].isdigit(): # Logic to fetch an entire number,
                num += inp[i]
                i += 1
            operand.append(int(num)) # push operand to stack
        elif inp[i] == '(': # if opening brace, push to stack
            operator.append(inp[i])
            i += 1
        elif inp[i] in operators: # if operator, pop all operators having a higher precedence
            while len(operator) and precedence(operator[-1]) >= precedence(inp[i]):
                b = operand.pop()
                a = operand.pop()
                op = operator.pop()
                operand.append(evlexp(a, b, op)) # evaluate them with the last 2 values in operand stack and append to itself
            operator.append(inp[i]) # append operator to operator stack)
            i += 1
        elif inp[i] == ')': # if closing brace, evaluate all operators in between
            while len(inp) != 0 and operator[-1] != '(': # while not EOF and the last(recent) item is not opening bracket
                b = operand.pop()
                a = operand.pop()
                op = operator.pop()
                operand.append(evlexp(a, b, op)) # pop the operator in order and evaluate and push to operand stack
            operator.pop() # pop (
            i += 1
        else:
            i += 1
            continue

    while len(operator) != 0: # while operator is not empty
        op = operator.pop()
        b = operand.pop()
        a = operand.pop()
        operand.append(evlexp(a, b, op)) # pop and evaluate operators till its empty and append to operand

    # if there are no more elements in top of stack, and only one (possibly the answer)
    if len(operand) == 1:
        return operand[-1]
    # if there's more than one element and no more operators, something wrong!
    else:
        raise ValueError
    



            
