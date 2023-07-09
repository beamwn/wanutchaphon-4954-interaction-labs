def get_operand(str):
    i = input(str)
    if i.lower() == 'q':
        exit()
    else: return float(i)

def get_operator():
    i = input("Enter an operation ('+', '-', '*', '/'):")
    if i not in ['-', '*', '/', '+', '']:
        print("Operation must be '+'','-','*' or '/'.")
        calculator()
    else: return i

def get_format():
    return input('Enter output format (float, int):')

def robust_calculator(op1, op2, operator, requested_format):
    if operator == '+' or operator == '':
        if requested_format == 'int':
            return round(op1) + round(op2)
        elif requested_format == 'float' or requested_format == '':
            return op1 + op2

    elif operator == '-':
        if requested_format == 'int':
               return round(op1) - round(op2)
        elif requested_format == 'float' or requested_format == '':
            return op1 - op2

    elif operator == '*':
        if requested_format == 'int':
               return round(op1) * round(op2)
        elif requested_format == 'float' or requested_format == '':
            return op1 * op2
    
    elif operator == '/':
        if op2 != 0:
            if requested_format == 'int':
                return round(op1) / round(op2)
            elif requested_format == 'float' or requested_format == '':
                return op1 / op2
        else:
            print('Cannot divide by zero')
            return None
ADD = '+'  

def calculator():
    while True:
        op1 = get_operand("Enter the first operand ('q' to quit):")
        op2 = get_operand("Enter the second operand ('q' to quit):")
        operator = get_operator()
        if operator is None:
            continue
        requested_format = get_format()
        output = robust_calculator(op1, op2, operator, requested_format)
        if output is not None:
            if operator == "":
                operator = ADD
            print("{} {} {} = {}".format(op1, operator, op2, output))
        else:
            print("We cannot perform your requested calculation")

if __name__ == "__main__":
    calculator()