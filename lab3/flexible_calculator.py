ADD = '+'
MUL = '*'
DIV = '/'
 
def flexible_calculator(operation, type, init, *args):
    try:
        for i in args:
            if(operation == ADD):
                init = i + init
            elif(operation == MUL):
                init = i * init
            elif(operation == DIV):
                init = init / i
        if type == int:
            return round(init)
        elif type == float:
            return init
    except ZeroDivisionError:
        print('Cannot divide 5 by zero')
        exit()

if __name__ == "__main__":
    print(f"flexible_calculator(ADD, int, 1) = {flexible_calculator(ADD, int, 1)}")
    print(f"flexible_calculator(ADD, int, 1, 2) = {flexible_calculator(ADD, int, 1, 2)}")
    print(f"flexible_calculator(ADD, int, 1, 2, 3, 4) = {flexible_calculator(ADD, int, 1, 2, 3, 4)}")
    print(f"flexible_calculator(MUL, int, 2, 3, 4) = {flexible_calculator(MUL, int, 2, 3, 4)}")
    print(f"flexible_calculator(DIV, float, 10, 5, 2) = {flexible_calculator(DIV, float, 10, 5, 2)}")
    print(f"flexible_calculator(DIV, float, 5,0) = {flexible_calculator(DIV, float, 5, 0)}")